import random

from src.facebook.create_content import create_comment, create_post_with_image
from src.utils.get_source_image import get_random_source


def create_poll_post():
    texts = [
        "Este gato es pendejo",
        "CUIDADO! Este gato es posible evador de impuesto",
        "¿Haz soñado con este hombre? Miles de personas sueñan todos los dias con este hombre, porfavor, si tienes alguna informacion porfavor y gracias",
        "CUIDADO\n Este gato es un 4s3s..1n0 en serie disfrazado de gato, muchos reportan que",
        "Que arias si me quito la camyssa frente aty\nte amo\nteodio\ntequiero",
        "ESTO NO ES UN GATO, ¡Mira bien!, ES UNA MUJER PINTADA",
    ]

    text = random.choice(texts) + "\n♥=Si 😲=No C 😡=No"
    image = get_random_source()
    post_id = create_post_with_image(content=text, image=image)

    create_comment(
        post_id=post_id, message="hola amigos como estan soy el bot los quiero mucho saludos soy el bot")
