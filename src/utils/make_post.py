import random

from src.utils.create_boomer_post import create_boomer_post
from src.utils.create_comparison_post import create_comparison_post
from src.utils.create_poll_post import create_poll_post

def make_post():
    post_themes = [create_boomer_post, create_comparison_post, create_poll_post]

    create_post = random.choice(post_themes)

    create_post()
