import cv2
import random

img = cv2.imread('assets/imgg.jpg', -1)
img = cv2.resize(img, (950, 950))

# print(img)
# print(type(img))
# print(img.shape)  # no. of rows(height), no. of columns(width), and no. of channels


# BGR(blue, green, red)
# [128, 0, 0] we are representing the pixel of the img

# print(img[257][400])  # first row

# Changing Pixel colors

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


# coping and pasting part of image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()