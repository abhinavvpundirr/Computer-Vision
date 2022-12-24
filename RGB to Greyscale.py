import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

img = mpimg.imread('/Users/abhinavpundir/Downloads/monkey-pixel-monkey-image-vector-illustration-pixel-art-monkey-pixel-monkey-image-vector-illustration-pixel-art-222374559.jpg')     
gray = rgb2gray(img)   
plt.imshow(gray, cmap='gray')
plt.show()