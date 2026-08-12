# Name: Foram Dholariya
# Assignment: Module 10 - Tkinter To-Do List


import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Window title and size
        self.title("Dholariya-ToDo")
        self.geometry("300x400")

        # Complementary colors: purple and yellow
        self.purple = "#A020F0"
        self.yellow = "#FFD700"

        # File menu
        menubar = tk.Menu(
            self,
            bg=self.purple,
            fg="white",
            activebackground=self.yellow,
            activeforeground="black"
        )

        file_menu = tk.Menu(
            menubar,
            tearoff=0,
            bg=self.purple,
            fg="white",
            activebackground=self.yellow,
            activeforeground="black"
        )

        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menubar)

        # Canvas and frames
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        # Create the instruction label
        instruction = tk.Label(
            self,
            text="** Right Click a Task to Delete **",
            bg=self.purple,
            fg="white",
            pady=10
        )
        instruction.pack(side=tk.TOP, fill=tk.X)

        # Text box for entering tasks
        self.task_create = tk.Text(
            self.text_frame,
            height=3,
            bg="white",
            fg="black"
        )

        # Pack canvas and scrollbar
        self.tasks_canvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
        )

        self.scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # Create frame inside canvas
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        # Pack text area
        self.task_create.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.text_frame.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.task_create.focus_set()

        # Add keyboard shortcut
        self.bind("<Return>", self.add_task)

        # Configure scrolling
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)

        # Make tasks fit the width of the window
        self.tasks_canvas.bind(
            "<Configure>",
            self.task_width
        )

        # Task color schemes
        self.colour_schemes = [
            {"bg": self.yellow, "fg": "black"},
            {"bg": self.purple, "fg": "white"}
        ]

    def add_task(self, event=None):
        task_text = self.task_create.get(
            1.0,
            tk.END
        ).strip()

        if len(task_text) > 0:

            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10
            )

            self.set_task_colour(
                len(self.tasks),
                new_task
            )

            # Right mouse button deletes the task
            new_task.bind(
                "<Button-3>",
                self.remove_task
            )

            new_task.pack(
                side=tk.TOP,
                fill=tk.X
            )

            self.tasks.append(new_task)

            self.task_create.delete(
                1.0,
                tk.END
            )

        return "break"

    def remove_task(self, event):
        task = event.widget

        if msg.askyesno(
            "Really Delete?",
            "Delete " + task.cget("text") + "?"
        ):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[
            task_style_choice
        ]

        task.configure(
            bg=my_scheme_choice["bg"]
        )

        task.configure(
            fg=my_scheme_choice["fg"]
        )

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def task_width(self, event):
        canvas_width = event.width

        self.tasks_canvas.itemconfig(
            self.canvas_frame,
            width=canvas_width
        )

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()