import time
import threading

from src.settings import BOT_POST_FREQUENCY

class Bot(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_flag = threading.Event()
        self.postFreq = BOT_POST_FREQUENCY

    def run(self) -> None:
        while not self.stop_flag.is_set():
            print('Thread is running.')
            time.sleep(self.postFreq)

    def stop(self) -> None:
        self.stop_flag.set()