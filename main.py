import dotenv

dotenv.load_dotenv()

import requests
import random
import time
import facebook
import os

from src.sources import cat_urls

# Configuración de la API de Facebook
token = os.getenv("token")
graph = facebook.GraphAPI(token)

# Función para obtener una imagen aleatoria de gato de CATAAS
def get_random_cat_url():
    return random.choice(cat_urls)

# Función para publicar una foto de gato en Facebook
def post_cat_photo():
    cat_url = get_random_cat_url()
    img_data = requests.get(cat_url).content
    graph.put_photo(image=img_data, message="CatMomo")
    print("Publicación realizada en Facebook a las ", time.strftime("%H:%M:%S"))

# Bucle principal del bot que publica una foto de gato cada 3 horas
while True:
    post_cat_photo()
    time.sleep(120*3)  # 3 horas
