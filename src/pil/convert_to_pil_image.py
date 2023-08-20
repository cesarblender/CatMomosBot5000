from PIL import Image
from io import BytesIO

def convert_to_pil_img(img):
    image = Image.open(BytesIO(img))

    return image
