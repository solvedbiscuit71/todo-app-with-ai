import { Routes } from '@angular/router';
import { TodoList } from './todo-list/todo-list';

export const routes: Routes = [
    {
        path: "",
        pathMatch: "full",
        redirectTo: "todos"
    },
    {
        path: "todos",
        component: TodoList
    },
];
