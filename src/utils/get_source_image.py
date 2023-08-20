import random
from src.sources.from_api import get_random_cat, get_picsum_photo


def get_random_source():
    return random.choice([get_random_cat(), get_picsum_photo()])
