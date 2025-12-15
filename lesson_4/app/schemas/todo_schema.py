from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str | None = Field(default=None)
    priority: int = Field(ge=1, le=5)
    done: bool = Field(default=False)


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3)
    description: str | None = None
    priority: int | None = Field(default=None, ge=1, le=5)
    done: bool | None = None


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None
    priority: int
    done: bool
