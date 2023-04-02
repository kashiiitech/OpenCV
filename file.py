import cv2

img = cv2.imread('assets/imgg.jpg', 0) # try other flags
img = cv2.resize(img, (400, 400))
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # try this: cv2.ROTATE_90_CLOCKWISE

# manipulated image will be saved
cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img )
cv2.waitKey(0)              # --> wait for infinity time new window will not be closed untill any keyboard button will be clicked.
cv2.destroyAllWindows()

# Img read flags
# 1 :: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag.
# 0 :: It specifies to load an image in grayscale mode.
# -1 :: It specifies to load an image as such including alpha channel.