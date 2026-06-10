from pydantic import BaseModel


class CreateTodoRequest(BaseModel):
    title: str
    description: str | None = None


class CreateTodoResponse(BaseModel):
    id: int
    message: str


class GetTodoResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool
