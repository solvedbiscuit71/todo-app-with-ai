from fastapi import FastAPI, HTTPException
from dto.todo import CreateTodoRequest, CreateTodoResponse, GetTodoResponse
from model.todo import TodoItem, TodoList

todo_list = TodoList()

app = FastAPI(root_path="/api/v1")

@app.post("/todo",  status_code=201)
async def create_todo(body: CreateTodoRequest) -> CreateTodoResponse:
    todo_item = TodoItem(body.title, body.description)
    todo_list.add(todo_item)

    return CreateTodoResponse(id=todo_item.id,
                              message="todo item created")

@app.get("/todo")
async def get_all_todos() -> list[GetTodoResponse]:
    return [
        GetTodoResponse(id=todo_item.id,
                        title=todo_item.title,
                        description=todo_item.description,
                        is_completed=todo_item.is_completed)
        for todo_item in todo_list
    ]

@app.get("/todo/{id}")
async def get_todo(id: int) -> GetTodoResponse:
    for todo_item in todo_list:
        if todo_item.id == id:
            return GetTodoResponse(id=todo_item.id,
                                   title=todo_item.title,
                                   description=todo_item.description,
                                   is_completed=todo_item.is_completed)
    raise HTTPException(status_code=404, detail=f"todo item #{id} is not found")