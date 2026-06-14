import { Component, inject, signal } from '@angular/core';
import { TodoService } from '../../services/todo';
import { TodoItem, TodoItemInfo } from '../todo-item/todo-item';
import { NewTodoForm } from "../new-todo-form/new-todo-form";

@Component({
  selector: 'app-todo-list',
  imports: [TodoItem, NewTodoForm],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.css',
})
export class TodoList {
  showNewTodo = signal<boolean>(false)
  todoList = signal<TodoItemInfo[]>([])
  todoService = inject(TodoService)

  constructor() {
    this.todoService.fetchAllTodos().then(this.todoList.set)
  }

  showForm() {
    this.showNewTodo.set(true)
  }

  hideForm() {
    this.showNewTodo.set(false)
  }
}
