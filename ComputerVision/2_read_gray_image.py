from copy import deepcopy
from pprint import pprint

import cv2
import constant

def change_bright(img, c=0):
    new_img = img.copy()
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            tmp = max(constant.MIN, min(constant.MAX, img[i, j] + c))
            new_img[i, j] = tmp
    return new_img

if __name__ == "__main__":
    # read image
    img = cv2.imread('images/mountain.jpeg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original img', img)

    c = 70
    #
    brighten_img = change_bright(img, c)
    cv2.imshow('brighten_img', brighten_img)


    darken_img = change_bright(img, -c)
    cv2.imshow('darken_img', darken_img)

    color_img = cv2.imread('images/mountain.jpeg')
    cv2.imshow('original color img', color_img)

    adjusted_img = color_img.copy()
    adjusted_img[:,:,0] = change_bright(adjusted_img[:,:,0], -70)
    adjusted_img[:,:,1] = change_bright(adjusted_img[:,:,1], -70)
    adjusted_img[:,:,2] = change_bright(adjusted_img[:,:,2], 70)
    cv2.imshow('adjusted_img, B -70, G -70 R 70', adjusted_img)

    adjusted_img = color_img.copy()
    adjusted_img[:,:,0] = change_bright(adjusted_img[:,:,0], -70)
    adjusted_img[:,:,1] = change_bright(adjusted_img[:,:,1], 70)
    adjusted_img[:,:,2] = change_bright(adjusted_img[:,:,2], -70)
    cv2.imshow('adjusted_img, B -70, G 70 R -70', adjusted_img)

    adjusted_img = color_img.copy()
    adjusted_img[:,:,0] = change_bright(adjusted_img[:,:,0], 70)
    adjusted_img[:,:,1] = change_bright(adjusted_img[:,:,1], -70)
    adjusted_img[:,:,2] = change_bright(adjusted_img[:,:,2], -70)
    cv2.imshow('adjusted_img, B 70, G -70 R -70', adjusted_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()