from exif import Image

with open("V:\\Foto-Film\\Jasper\\j.jpg", "rb") as image_file:
    img = Image(image_file)
print(dir(img))


