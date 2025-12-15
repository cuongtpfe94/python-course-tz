from fastapi import FastAPI
from app.controllers import todo_controller

app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(todo_controller.router)


@app.get("/")
def root():
    return {
        "message": "Todo API",
        "docs": "/docs",
        "endpoints": {
            "create": "POST /todos",
            "get_all": "GET /todos",
            "get_by_id": "GET /todos/{id}",
            "update_full": "PUT /todos/{id}",
            "update_partial": "PATCH /todos/{id}",
            "delete": "DELETE /todos/{id}",
        },
    }
