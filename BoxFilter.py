import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def addboxfilter(image):
        offset=5
        image_padded=np.pad(image,((offset,offset),(offset,offset),(0,0)),mode='constant')
        h , w ,_= image_padded.shape
        g=np.zeros(image_padded.shape,dtype=np.int32)
        kernel_size=11
        for k in range(3):
            for i in range(offset,h-offset):
                for j in range (offset,w-offset):
                    kmatx=image_padded[i-offset:(i-offset+kernel_size),j-offset:(j-offset+kernel_size),k]
                    g[i][j][k]=int(kmatx.sum()/(kernel_size**2))
        return g.astype("int32")
img = mpimg.imread('/Users/abhinavpundir/Downloads/monkey-pixel-monkey-image-vector-illustration-pixel-art-monkey-pixel-monkey-image-vector-illustration-pixel-art-222374559.jpg')
g=addboxfilter(img)
plt.imshow(g)
plt.show()