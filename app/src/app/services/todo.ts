import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { TodoItemInfo } from '../todo-item/todo-item';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  baseUrl = environment.apiUrl

  async fetchAllTodos() {
    const data = await fetch(this.baseUrl + "/todo", { method: "GET" })
    const todos: TodoItemInfo[] = await data.json()

    return todos
  }
}
