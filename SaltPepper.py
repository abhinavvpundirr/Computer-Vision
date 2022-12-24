import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

def add_salt_pepper(img):
    row , col = img.shape[0],img.shape[1]
    totalnumberofpixels=row*col
    number_of_pixels_salt = int(0.1*totalnumberofpixels)
    for i in range(number_of_pixels_salt):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        img[y][x] = 255
    number_of_pixels_pepper = int(0.3*totalnumberofpixels)
    for i in range(number_of_pixels_pepper):
        y=random.randint(0, row - 1)
        x=random.randint(0, col - 1)
        img[y][x] = 0    
    return img
img = mpimg.imread('/Users/abhinavpundir/Downloads/train2.png')
g=add_salt_pepper(img)
plt.imshow(g)
plt.show()