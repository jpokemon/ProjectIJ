from exif import Image

with open(".\\test.jpg", "rb") as image_file:
    img = Image(image_file)
print(dir(img))


