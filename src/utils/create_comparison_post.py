from io import BytesIO

from src.sources.from_api import get_picsum_photo, get_random_cat
from src.pil.convert_to_pil_image import convert_to_pil_img
from pil.create_comparison_image import create_comparison_image
from src.facebook.create_content import create_comment, create_post_with_image


def create_comparison_post():
    comparison_image = create_comparison_image(convert_to_pil_img(
        get_random_cat()), convert_to_pil_img(get_picsum_photo()))
    
    buffer = BytesIO()
    comparison_image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()

    post_id = create_post_with_image(content="Comparison Momo", image=image_bytes)

    create_comment(post_id=post_id, message="hola amigos soy el bot los quiero saludos soy el bot.")

    return post_id
