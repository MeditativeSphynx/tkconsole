import tkinter as tk

from Console import q


class Root(tk.Tk):
    def __init__(self, title=None):
        super().__init__()
        self.geometry('700x700')
        self.title = title if title is not None else 'Console'


class ConsoleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.output_queue = q
