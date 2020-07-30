import hashlib
from queue import Queue
from random import randint
from time import sleep, time
from threading import Thread

from faker import Faker

from Console import interface

QUEUE = Queue(100)


class DataGen:
    STOP_FLAG = False
        
    def hash_data(self, val):
        val_str = str(val)
        return hashlib.md5(val_str.encode()).hexdigest(), val_str

    def stop(self):
        self.STOP_FLAG = True

    def data_generation(self):
        faker = Faker()
        total_time = 0
        start = time()
        while True:
            # Set the string and hash values
            val_hash, val_str = self.hash_data(faker.password())
            val_hash_combo = f'{val_hash}:{val_str}'

            # Queue them up for output
            # TODO: Find a way to remove the necessity of this sleep. If this 
            #   isn't here, the tkinter window freezes. Although the window
            #   freezes the methods behind the scenes run normally. 
            sleep(.000001)
            QUEUE.put(val_hash_combo)

            total_time = time() - start
            self.STOP_FLAG = True if total_time > 1 else self.STOP_FLAG
            if self.STOP_FLAG: break
        QUEUE.put('data generation is complete...')


if __name__ == '__main__':
    dg = DataGen()
    data_thread = Thread(target=dg.data_generation)

    ui_root = interface.Root()
    console_frame = interface.ConsoleFrame(ui_root, QUEUE)

    data_thread.start()
    ui_root.mainloop()

    dg.stop()
