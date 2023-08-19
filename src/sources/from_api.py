import random
import requests

source_images = {
    "flattened": "https://cataas.com/cat?width=420&height=100",
    "square": "https://cataas.com/cat?type=sq",
    "pixel": "https://cataas.com/cat?filter=pixel",
    "normal": "https://cataas.com/cat"
}

def get_random_cat():
    keys = source_images.keys()
    source = random.choice(keys)

    source_image = source_images[source]

    response = requests.get(source_image)

    return response.content

def get_cat(source_type: str):
    keys = source_images.keys()
    if source_type not in keys:
        raise KeyError(source_type + " Is not in source_images.keys()")
    
    source_image = source_images[source_type]

    response = requests.get(source_image)

    return response.content
