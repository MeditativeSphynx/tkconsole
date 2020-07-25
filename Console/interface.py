import tkinter as tk
from Console import q

class Root(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.geometry = '700x800'


class ConsoleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.output_queue = q
