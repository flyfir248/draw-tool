import string
from PIL import Image, ImageDraw, ImageFont
import random

# Generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate an image with a random color and a random string of text
def generate_image():
    # Create a new image with a random color
    image = Image.new('RGB', (200, 200), random_color())

    # Create a draw object
    draw = ImageDraw.Draw(image)

    # Generate a random string of text
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Get a font
    font = ImageFont.truetype('arial.ttf', 36)

    # Draw the text on the image
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))

    return image

# Generate and save an image
image = generate_image()
image.save('image.jpg')

