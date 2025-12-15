from fastapi import HTTPException
from datetime import datetime
from app.models.todo import Todo
from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoOut

_todos: list[Todo] = []
_id_counter = 1


def create_todo(todo_data: TodoCreate) -> TodoOut:
    global _id_counter

    if any(todo.title.lower() == todo_data.title.lower() for todo in _todos):
        raise HTTPException(status_code=409, detail="Todo title already exists")

    new_todo = Todo(
        id=_id_counter,
        title=todo_data.title,
        description=todo_data.description,
        priority=todo_data.priority,
        done=todo_data.done,
        created_at=datetime.now(),
    )

    _todos.append(new_todo)
    _id_counter += 1

    return TodoOut(**new_todo.model_dump())


def get_all_todos(
    done: bool | None = None, keyword: str | None = None, limit: int = 10
) -> list[TodoOut]:
    result = _todos.copy()

    if done is not None:
        result = [todo for todo in result if todo.done == done]
    if keyword:
        result = [todo for todo in result if keyword.lower() in todo.title.lower()]

    result = result[:limit]

    return [TodoOut(**todo.model_dump()) for todo in result]


def get_todo_by_id(id: int) -> TodoOut | None:
    for todo in _todos:
        if todo.id == id:
            return TodoOut(**todo.model_dump())
    return None


def update_todo(id: int, todo_data: TodoCreate) -> TodoOut | None:
    for i, todo in enumerate(_todos):
        if todo.id == id:
            updated_todo = Todo(
                id=id,
                title=todo_data.title,
                description=todo_data.description,
                priority=todo_data.priority,
                done=todo_data.done,
                created_at=todo.created_at,
            )
            _todos[i] = updated_todo
            return TodoOut(**updated_todo.model_dump())

    return None


def update_todo_partial(id: int, todo_data: TodoUpdate) -> TodoOut | None:
    for i, todo in enumerate(_todos):
        if todo.id == id:
            if todo_data.title is not None:
                todo.title = todo_data.title
            if todo_data.description is not None:
                todo.description = todo_data.description
            if todo_data.priority is not None:
                todo.priority = todo_data.priority
            if todo_data.done is not None:
                todo.done = todo_data.done

            return TodoOut(**todo.model_dump())

    return None


def delete_todo(id: int) -> bool:
    for i, todo in enumerate(_todos):
        if todo.id == id:
            _todos.pop(i)
            return True
    return False
