import numpy as np
import imageio.v3 as iio
import cv2

im = iio.imread('terr-fish.jpeg')
print(im.shape)
print(type(im))

rudimentary_image = np.asarray([[[256, 0,   0], [0, 256, 0]], [[0, 0, 256], [0, 0, 0]]])
print(rudimentary_image.shape)
rud_image_read = iio.imread(rudimentary_image)
cv2.imwrite("filename.png", rudimentary_image)
print(rud_image_read.shape)