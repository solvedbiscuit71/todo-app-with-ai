from fastapi import FastAPI, HTTPException
from dto.todo import CreateTodoRequest, CreateTodoResponse, GetTodoResponse
from model.todo import TodoItem 
from peewee import DoesNotExist

app = FastAPI(root_path="/api/v1")

@app.post("/todo",  status_code=201)
async def create_todo(body: CreateTodoRequest) -> CreateTodoResponse:
    todo_item = TodoItem.create(title=body.title, description=body.description)

    return CreateTodoResponse(id=todo_item.id,
                              message="todo item created")

@app.get("/todo")
async def get_all_todos() -> list[GetTodoResponse]:
    return [
        GetTodoResponse(id=todo_item.id,
                        title=todo_item.title,
                        description=todo_item.description,
                        is_completed=todo_item.is_completed)
        for todo_item in TodoItem.select()
    ]

@app.get("/todo/{id}")
async def get_todo(id: int) -> GetTodoResponse:
    try:
        todo_item = TodoItem.get_by_id(id)
        return GetTodoResponse(id=todo_item.id,
                                title=todo_item.title,
                                description=todo_item.description,
                                is_completed=todo_item.is_completed)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"todo item #{id} is not found")