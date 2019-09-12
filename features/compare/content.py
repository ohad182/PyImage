import cv2
import numpy as np


def is_same_content(img1_path, img2_path, compare_mode=1) -> bool:
    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)
    # Option 1
    if compare_mode == 1:
        return compare1(image1, image2)
    elif compare_mode == 2:
        return compare2(image1, image2)


def compare1(cv_img1, cv_img2) -> bool:
    # verify they both have same shape
    if cv_img1.shape == cv_img2.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(cv_img1, cv_img2)
        b, g, r = cv2.split(difference)
        return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
    return False


def compare2(cv_img1, cv_img2):
    difference = cv2.subtract(cv_img1, cv_img2)
    result = not np.any(difference)
    return result
