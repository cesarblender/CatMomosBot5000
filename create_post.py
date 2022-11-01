from python_easy_facebook_api import FbApi
import requests
import os
from flask import Flask

app = Flask(__name__)

api = FbApi(page_id=os.environ["PAGE_ID"], access_token=os.environ["TOKEN"])


def createCatPost():
    print("Uploading request to Facebook Graph API...")
    photo = requests.get(
        url="https://api.thecatapi.com/v1/images/search"
    ).json()[0]['url']

    r = api.TextWithPhotoPost(
        image_url=photo,
        content="Random cat\nBot source code: https://github.com/seokkuuu/RandomCatBot\nLirary used: https://github.com/seokkuuu/python_easy_facebook_api\nLibrary package url: https://pypi.org/project/python-easy-facebook-api\n\nApp made by:\nhttps://facebook.com/seokkuxd\nhttps://github.com/seokkuuu\n"
    ).submitPost()

    print(r.text)
    print("Post uploaded successfully!")
