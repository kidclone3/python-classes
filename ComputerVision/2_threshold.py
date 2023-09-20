from copy import deepcopy
from pprint import pprint

import cv2
import constant
from collections import deque as queue

def thresholding(img, threshold):
    new_img = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > threshold:
                new_img[i, j] = constant.MAX
            else:
                new_img[i, j] = constant.MIN
    return new_img

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(img, visited, i, j, threshold):
    q = queue()
    q.append((i, j))
    min_i_j = [img.shape[0], img.shape[1]]
    max_i_j = [-1, -1]
    visited.add((i, j))
    while len(q) > 0:
        i, j = q.popleft()
        min_i_j = [min(min_i_j[0], i), min(min_i_j[1], j)]
        max_i_j = [max(max_i_j[0], i), max(max_i_j[1], j)]
        for d in directions:
            new_i, new_j = i + d[0], j + d[1]
            if (new_i, new_j) not in visited and 0 <= new_i < img.shape[0] and 0 <= new_j < img.shape[1] and img[i,j] == threshold:
                q.append((new_i, new_j))
                visited.add((new_i, new_j))
    return min_i_j, max_i_j
def draw_text_box(img):
    contour_img = img.copy()
    visited = set()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == constant.MIN:
                min_pos, max_pos = bfs(img, visited, i, j, constant.MIN)
                cv2.rectangle(contour_img, (min_pos[1], min_pos[0]), (max_pos[1], max_pos[0]), (50, 0, 0), 2)
    return contour_img

if __name__ == "__main__":
    # read image
    img = cv2.imread('images/l002-social.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('original img', img)
    print(img.shape)
    threshold = 170
    thresholding_img = thresholding(img, threshold)
    cv2.imshow('thresholding_img', thresholding_img)
    #
    contoured_img = draw_text_box(thresholding_img)
    cv2.imshow('contoured_img', contoured_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()