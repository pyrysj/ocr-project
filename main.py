from PIL import Image 

import pillow_heif

import pytesseract

heif_file = pillow_heif.read_heif('images/test.heic')
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",
)

image.save("images/test.jpeg", format("jpeg"))


# code required to make heif work


print(pytesseract.image_to_string(image,lang='jpn'))

print(pytesseract.image_to_string('images/test.jpeg',lang='jpn'))