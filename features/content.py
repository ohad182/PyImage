import cv2
import numpy as np


def is_same_content(img1_path, img2_path)
    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    # verify they both have same shape
    if image1.shape == image2.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(image1, image2)
        b, g, r = cv2.split(difference)

        return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
