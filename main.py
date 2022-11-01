from python_easy_facebook_api import FbApi
import requests
import os
import sched, time
from flask import Flask
import threading

app = Flask(__name__)

api = FbApi(page_id=os.environ["PAGE_ID"], access_token=os.environ["TOKEN"])


def createCatPost():
    photo = requests.get(
        "https://api.thecatapi.com/v1/images/search").json()[0]['url']

    r = api.TextWithPhotoPost(image_url=photo,
                              content="Random cat").submitPost()

    print(r.text)

print("Creating...")
createCatPost()
print("Created!")


@app.route('/')
def index():
    return 'Hello from Flask!'

def initServer():
  app.run(host='0.0.0.0', port=81)


s = sched.scheduler(time.time, time.sleep)
delay = 60 * 20


def repeat(sc):
    print("Creating...")
    createCatPost()
    print("Created!")
    sc.enter(delay, 1, repeat, (sc, ))

def initRepeat():
  s.enter(delay, 1, repeat, (s, ))
  s.run()

t1 = threading.Thread(target=initServer)
t2 = threading.Thread(target=initRepeat)

t1.start()
t2.start()
