import time
import tkinter as tk
from tkinter.font import Font
from threading import Thread


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
        print('[get_data]')
        while not self.q.empty():
            value = self.q.get()
            # print('[getting]', value)

            try:
                Thread(target=self.update_text, args=(value,)).start() 
                # TODO: RUNTIME ERROR OCCURS BECAUSE IT IS TRYING TO START A NEW
                #   THREAD WITH THE SAME VARIABLE FROM THE PREVIOUS VARIABLE 
                #   THAT IS STILL ALIVE
            except RuntimeError:
                print('[RuntimeError]')
                break



            self.q.task_done()
            if self.q.empty(): break
            
        self.after(100, self.get_data)

    def update_text(self, value):
        print('[value]', value)
        self.text.insert(tk.END, f'[getting ({self.count})] ' + value + '\n')
        self.text.see(tk.END)
        self.count += 1