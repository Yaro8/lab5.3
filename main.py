from PIL import Image, ImageGrab


def mirror(n):
    im = Image.open(n)
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im.save('res.jpg')
    im.show()


img_orig = ImageGrab.grab()
img_orig.save('image.jpg')
mirror('image.jpg')

