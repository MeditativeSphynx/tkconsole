import tkinter as tk


class Root(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.geometry = '700x800'
