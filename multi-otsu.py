# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 00:07:58 2024

@author: SUBHADIP HENSH
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage import data,io,img_as_ubyte
from skimage.filters import threshold_multiotsu

# read an image

img = io.imread("E:/Pictures/Saved Pictures/nature.jfif")    # you can add image path here
plt.imshow(img)

thresholds = threshold_multiotsu(img,classes = 5)

regions = np.digitize(img,bins=thresholds)
output = img_as_ubyte(regions)

#Let us look at the input image, thresholds on the histogram and final segmented image
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))

# Plotting the original image.
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original')
ax[0].axis('off')

# Plotting the histogram and the two thresholds obtained from
# multi-Otsu.
ax[1].hist(img.ravel(), bins=255)
ax[1].set_title('Histogram')
for thresh in thresholds:
    ax[1].axvline(thresh, color='r')

# Plotting the Multi Otsu result.
ax[2].imshow(regions, cmap='Accent')
ax[2].set_title('Multi-Otsu result')
ax[2].axis('off')

plt.subplots_adjust()

plt.show()
