from exif import Image

with open("C:\\Users\\igor\\OneDrive\\Git\\github.com\\jpokemon\\ProjectIJ\\test.jpg", "rb") as image_file:
    img = Image(image_file)
print(dir(img))


