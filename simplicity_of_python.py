from skimage import io, filters
from matplotlib import pyplot as plt
img = io.imread('E:\\Pictures\\Saved Pictures\\nature_edited.jpg')
gaussian_img = filters.gaussian(img,sigma = 2)
plt.imshow(gaussian_img)
plt.show() 