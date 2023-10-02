from PIL import Image, ImageFilter

img = Image.open('./images/bulbasaur.jpg')

newImg = img.filter(ImageFilter.BLUR)

# newImg.save('new.jpg')

newImg.show()