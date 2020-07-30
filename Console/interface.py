import time
import tkinter as tk
from tkinter.font import Font


class Root(tk.Tk):
    def __init__(self, title=None):
        super().__init__()
        self.geometry('700x700')
        self.title = title if title is not None else 'Console'


class ConsoleFrame(tk.Frame):
    def __init__(self, master, q):
        super().__init__(master)
        self.font = Font(family='Cascadia Code', size=11)
        # self.font = Font(family='Fira Mono', size=11)
        self.master = master
        self.q = q

        self.count = 0

        self.pack(fill=tk.BOTH, expand=1)

        self.text = tk.Text(self)
        self.text['font'] = self.font
        self.text['bg'] = 'black'
        self.text['fg'] = 'white'
        self.text.pack(fill=tk.BOTH, expand=1)

        self.after(5, self.get_data)  # TODO: MAKE THIS A THREAD

    def get_data(self):
        while not self.q.empty():
            value = self.q.get()
            self.update_text(value)
            self.q.task_done()
            if self.q.empty(): break
            
        self.after(100, self.get_data)

    def update_text(self, value):
        self.count += 1
        self.text.insert(tk.END, f'[getting ({self.count})] ' + value + '\n')
        self.text.see(tk.END)
