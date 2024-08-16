import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("450x450")
        self.root.config(bg="#f7f7f7")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 24, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=10)

        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, font=("Arial", 14), width=25, height=10, selectbackground="#a6a6a6", bg="#eaeaea")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.task_frame) 
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, font=("Arial", 14), width=20)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", font=("Arial", 14), bg="#5bc0de", fg="#fff", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.update_button = tk.Button(self.button_frame, text="Update Task", font=("Arial", 14), bg="#5bc0de", fg="#fff", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=("Arial", 14), bg="#d9534f", fg="#fff", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.done_button = tk.Button(self.button_frame, text="Mark as Done", font=("Arial", 14), bg="#5cb85c", fg="#fff", command=self.mark_as_done)
        self.done_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            if not task.startswith("✔"):
                self.tasks[selected_task_index[0]] = "✔ " + task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
