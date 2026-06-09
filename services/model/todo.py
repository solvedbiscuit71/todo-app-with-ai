from typing import ClassVar

class IntSequence:
    value: int

    def __init__(self, initial_value: int) -> None:
        self.value = initial_value

    def __next__(self):
        next_value = self.value
        self.value += 1
        return next_value

class TodoItem:
    _id_seq: ClassVar[IntSequence] = IntSequence(1001)

    id: int
    title: str
    description: str | None
    is_completed: bool

    def __init__(self, title: str, description: str | None = None) -> None:
        self.id = next(TodoItem._id_seq)
        self.title = title
        self.description = description
        self.is_completed = False
    
    def __repr__(self) -> str:
        return f"TodoItem(id={self.id}, title='{self.title}', is_completed={self.is_completed})"

class TodoList:
    todos: list[TodoItem]

    def __init__(self) -> None:
        self.todos = []

    def add(self, todo: TodoItem):
        self.todos.append(todo)

    def __iter__(self):
        return iter(self.todos)