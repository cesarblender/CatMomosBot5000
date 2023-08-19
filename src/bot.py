import time
import threading

from src.settings import BOT_POST_FREQUENCY
from src.utils.make_post import make_post

class Bot(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_flag = threading.Event()
        self.postFreq = BOT_POST_FREQUENCY

    def run(self) -> None:
        while not self.stop_flag.is_set():
            make_post()
            time.sleep(self.postFreq)

    def stop(self) -> None:
        self.stop_flag.set()