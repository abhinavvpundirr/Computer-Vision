import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def addnoise(image,sd):
    n = np.random.normal(loc=0,scale=sd,size=image.shape).astype("int32")
    g = image + n 
    return g
img = mpimg.imread('/Users/abhinavpundir/Downloads/Figure_1.png')
sd=(float)(input('Please enter Standard Deviation'))
g=addnoise(img,sd)
plt.imshow(g)
plt.show()