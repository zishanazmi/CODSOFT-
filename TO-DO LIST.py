import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, height=15, width=50)
        self.tasks_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.clear_all_button = tk.Button(root, text="Clear All", command=self.clear_all)
        self.clear_all_button.pack(pady=5)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks = []
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
