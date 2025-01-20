import tkinter as tk
from tkinter import messagebox
import time

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        self.completed_tasks = []

        # Frame for the task input and buttons
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.delete_task_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT)

        self.complete_task_button = tk.Button(self.frame, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(side=tk.LEFT)

        # Listbox to display current tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Listbox to display completed tasks
        self.completed_listbox = tk.Listbox(self.root, width=50, height=10)
        self.completed_listbox.pack(pady=10)

        # Display current time
        self.time_label = tk.Label(self.root, text="")
        self.time_label.pack(pady=10)

        self.update_time()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_task_index]
            self.completed_tasks.append(completed_task)
            del self.tasks[selected_task_index]
            self.update_task_listbox()
            self.update_completed_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def update_completed_listbox(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_tasks:
            self.completed_listbox.insert(tk.END, task)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)  # Update time every second

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
