import sched
import time
import threading

from create_post import createCatPost
from server import startServer

s = sched.scheduler(time.time, time.sleep)
delay = 5  # Every 20 minutes


def repeat(sc):
    createCatPost()
    sc.enter(delay, 1, repeat, (sc, ))


createCatPost()


def initRepeat():
    s.enter(delay, 1, repeat, (s, ))
    s.run()


"""
The problem with having many processes is that the program can only run one process at a time.
The solution is to run that process in parallel, using another CPU thread
"""

# Define the threads
server_thread = threading.Thread(target=startServer)
repeat_post_upload_thread = threading.Thread(target=initRepeat)

# Start the threads
server_thread.start()

repeat_post_upload_thread.start()
