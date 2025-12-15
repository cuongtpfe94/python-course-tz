from pydantic import BaseModel, Field
from datetime import datetime


class Todo(BaseModel):
    id: int
    title: str = Field(min_length=3)
    description: str | None = Field(default=None)
    priority: int = Field(ge=1, le=5)
    done: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
