from src.facebook.create_content import create_comment, create_post_with_image
from src.ai.bloom import gen_boomer_text
from src.utils.get_source_image import get_random_source
from src.utils.get_info import get_info

def create_boomer_post():
    text, params = gen_boomer_text()
    image = get_random_source()
    post_id = create_post_with_image(content=text, image=image)

    create_comment(post_id=post_id, message=get_info(params, "External API"))
