from PIL import Image, ImageDraw, ImageFont


def create_comparison_image(image1, image2):
    image_width = 1200
    image_height = 630

    image = Image.new("RGB", (image_width, image_height), "white")

    resized_image1 = image1.resize(
        (image_width // 2, image_height-100), Image.BILINEAR)
    resized_image2 = image2.resize(
        (image_width // 2, image_height-100), Image.BILINEAR)
    image.paste(resized_image1, (0, 100))
    image.paste(resized_image2, (image_width // 2, 100))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("./src/fonts/Roboto-Regular.ttf", size=35)
    text = "¡ELLOS SE PARECEN MAS DE LO QUE TU CREES!\n>>Haz clic aquí para más información<<"
    draw.text((image_height, 100/2), text,
              font=font, fill="black", anchor="mm", align="center")

    return image
