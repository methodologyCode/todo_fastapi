from typing import Union

from pydantic import BaseModel


class TodoModel(BaseModel):
    title: str
    description: str
    completed: Union[bool, None] = None
