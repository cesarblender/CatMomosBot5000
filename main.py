import requests
import random
import time
import facebook
import os

# Configuración de la API de Facebook
token = os.getenv("token")
graph = facebook.GraphAPI(token)

# URL de las imágenes de gatos en CATAAS
cat_urls = [
    "https://cataas.com/cat/cute/says/random%20cat%20bot",
    "https://cataas.com/cat/says/random%20cat%20bot",
    "https://cataas.com/cat/says/random%20cat%20bot?filter=pixel",
    "https://picsum.photos/64/64"
]

# Función para obtener una imagen aleatoria de gato de CATAAS
def get_random_cat_url():
    return random.choice(cat_urls)

# Función para publicar una foto de gato en Facebook
def post_cat_photo():
    cat_url = get_random_cat_url()
    img_data = requests.get(cat_url).content
    graph.put_photo(image=img_data, message="CatMomo")
    print("Publicación realizada en Facebook a las ", time.strftime("%H:%M:%S"))
# Bucle principal del bot que publica una foto de gato cada 30 minutos
while True:
    post_cat_photo()
    time.sleep(120*3)  # 3 horas
