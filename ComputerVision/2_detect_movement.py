from pprint import pprint

import cv2
import numpy as np
import constant
from numba import jit, njit


@jit
def thresholding(img, threshold):
    new_img = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > threshold:
                new_img[i, j] = constant.MAX
            else:
                new_img[i, j] = constant.MIN

    return new_img

@jit
def compare_two_img(img1, img2):
    new_img = img2.copy()
    new_img = abs(img1 - img2)
    return new_img

if __name__ == "__main__":
    cap = cv2.VideoCapture() # Create a VideoCapture object
    cap.open(0) # read from the first camera
    # cap.open("https://129.226.145.57:7548/")
    # create 3 squares
    delta = 50
    ret, frame = cap.read()
    print(f"{ret=}, {frame.shape=}")
    old_img = None
    while True:
        if cv2.waitKey(1) == ord('q'):
            break
        ret, frame = cap.read()
        # frame = cv2.resize(frame, (300, 300))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            break
        if old_img is None:
            old_img = frame
            continue

        image_diff = compare_two_img(frame, old_img)
        thresholding_img = thresholding(image_diff, 50)


        cv2.imshow("video", frame)
        # cv2.imshow("image_diff", image_diff)
        cv2.imshow("thresholding_img", thresholding_img)
        old_img = frame
        cv2.waitKey(20)
