from fastapi import APIRouter, HTTPException, Query, status
from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoOut
from app.services import todo_service

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    return todo_service.create_todo(todo)


@router.get("", response_model=list[TodoOut])
def get_todos(
    done: bool | None = Query(default=None),
    keyword: str | None = Query(default=None),
    limit: int = Query(default=10, ge=1, le=50),
):
    return todo_service.get_all_todos(done=done, keyword=keyword, limit=limit)


@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    todo = todo_service.get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo: TodoCreate):
    updated = todo_service.update_todo(todo_id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@router.patch("/{todo_id}", response_model=TodoOut)
def partial_update_todo(todo_id: int, todo: TodoUpdate):
    updated = todo_service.update_todo_partial(todo_id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    success = todo_service.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
