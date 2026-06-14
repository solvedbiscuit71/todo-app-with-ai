import { Component, input } from '@angular/core';

export interface TodoItemInfo {
  id: number,
  title: string,
  description: string | null,
  isCompleted: boolean,
}

@Component({
  selector: 'app-todo-item',
  imports: [],
  templateUrl: './todo-item.html',
  styleUrl: './todo-item.css',
})
export class TodoItem {
  value = input.required<TodoItemInfo>()
}
