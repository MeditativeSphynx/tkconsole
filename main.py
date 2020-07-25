from time import sleep

from faker import Faker

from Console import interface
from Console import q


if __name__ == '__main__':
    ui_root = interface.Root(title='Sign Ups')
    console_frame = interface.ConsoleFrame(ui_root)
    ui_root.mainloop()