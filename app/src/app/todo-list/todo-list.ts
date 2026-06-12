import { Component, inject, signal } from '@angular/core';
import { TodoService } from '../services/todo';
import { TodoItem, TodoItemInfo } from '../todo-item/todo-item';

@Component({
  selector: 'app-todo-list',
  imports: [TodoItem],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.css',
})
export class TodoList {
  todoList = signal<TodoItemInfo[]>([])
  todoService = inject(TodoService)

  constructor() {
    this.todoService.fetchAllTodos().then(this.todoList.set)
  }
}
