import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.9, fy=0.9)  # resizing for shoe
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.9, fy=0.9)   # change it to shoe
h, w = template.shape

# methods for doing template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# according to documentation we will try and find the best method

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    # (W - w + 1, H - h + 1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # draw the rectangle in the base image
    # top left
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # bottom right
    bottom_right = (location[0] + w, location[1] + h)


    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()