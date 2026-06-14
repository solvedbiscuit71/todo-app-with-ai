import { Component, inject, output } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-new-todo-form',
  imports: [ReactiveFormsModule],
  templateUrl: './new-todo-form.html',
  styleUrl: './new-todo-form.css',
})
export class NewTodoForm {
  cancelled = output<void>();

  private formBuilder = inject(FormBuilder);

  newTodoForm = this.formBuilder.group({
    title: ['', [Validators.required, Validators.maxLength(100)]],
    description: ['', Validators.maxLength(512)]
  })

  onSubmit() {
    if (this.newTodoForm.valid) {
      console.log(this.newTodoForm.value)
    }
  }

  onReset() {
    this.cancelled.emit()
  }
}
