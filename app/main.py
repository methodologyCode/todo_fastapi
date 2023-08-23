from fastapi import (
    FastAPI,
    Response,
    status,
    HTTPException,
)

from db import models
from db.database import engine
from db.service import SqliteTools
from schemas import TodoModel

app = FastAPI()
models.Base.metadata.create_all(engine)


@app.get("/todo/{todo_id}/", status_code=status.HTTP_200_OK)
def get_todo_by_id(todo_id: int):
    todo = SqliteTools.get_todo_by_id(todo_id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )

    return todo


@app.post("/todo/", status_code=status.HTTP_201_CREATED)
def create_todo(todo_data: TodoModel):
    todo = SqliteTools.add_todo(todo_data.title, todo_data.description,
                                todo_data.completed)
    return todo


@app.put("/todo/{todo_id}/", status_code=status.HTTP_200_OK)
def update_todo_by_id(todo_id: int, todo_data: TodoModel):
    todo = SqliteTools.update_todo_by_id(
        todo_id, todo_data.title, todo_data.description, todo_data.completed
    )

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )

    return todo


@app.delete("/todo/{todo_id}/")
async def delete_todo_by_id(todo_id: int):
    deleted = SqliteTools.delete_todo_by_id(todo_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
