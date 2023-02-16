import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello_label = tk.Label(self, text="Hello, world!")
        self.hello_label.pack(side="top")
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()