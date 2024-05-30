from PIL import Image
import os
import base64
from PIL import Image
from io import BytesIO

def base64_to_image(base64_string):
    # Remove the data URI prefix if present
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]

    # Decode the Base64 string into bytes
    image_bytes = base64.b64decode(base64_string)
    return image_bytes


def create_image_from_bytes(image_bytes):
    # Create a BytesIO object to handle the image data
    image_stream = BytesIO(image_bytes)

    # Open the image using Pillow (PIL)
    image = Image.open(image_stream)
    return image

def compress_image(image_name):
    image = Image.open(image_name)

    width, height = image.size
    new_size = (width//2, height//2)
    resized_image = image.resize(new_size)

    resized_image.save('compressed_image.jpg', optimize=True, quality=50)

    original_size = os.path.getsize('image.jpg')
    compressed_size = os.path.getsize('compressed_image.jpg')

    print("Original Size: ", original_size)
    print("Compressed Size: ", compressed_size)


def image_to_base64(image_name):
    # Open the image file
    with open(image_name, "rb") as f:
        image = Image.open(f)

    # Convert the image to base64 format
    with open(image_name, "rb") as f:
        encoded_image = base64.b64encode(f.read())

    # Save the encoded image to a file
    with open("image.txt", "w") as f:
        f.write(encoded_image.decode("utf-8"))

def main():
    # Replace this with your Base64 string
    base64_string = "your_base64_string_here"

    # Convert Base64 to image bytes
    image_bytes = base64_to_image(base64_string)

    # Create an image from bytes
    img = create_image_from_bytes(image_bytes)

    # Display or save the image as needed
    img.show()
    # img.save("output_image.jpg")
