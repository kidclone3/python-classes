from copy import deepcopy
from pprint import pprint

import cv2
import numpy as np

import constant
from matplotlib import pyplot as plt


def histogram(img):
    hist = [0 for _ in range(256)]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i, j]] += 1
    t_hist = [0 for _ in range(256)]
    t_hist[0] = hist[0]
    for i in range(1, 256):
        t_hist[i] = t_hist[i-1]+hist[i]

    return hist, t_hist

def histogram_equalization(img, t_hist, new_level):
    mean = img.shape[0]*img.shape[1] // new_level
    f = [max(0, round(t_hist[i]/mean)-1) for i in range(256)]
    new_img = img.copy()
    for i in range(new_img.shape[0]):
        for j in range(new_img.shape[1]):
            new_img[i][j] = f[img[i][j]]
    return new_img

def draw_histogram(hist, h=300, w=256, H = 300, color=[255, 255, 255]):
    max_hist = max(hist)
    plane = np.zeros((h, w, 3), np.uint8)
    for i, val in enumerate(hist):
        v = val*H//max_hist
        for j in range(v):
            plane[-j][i] = color
    return plane

def draw_histogram_plt(hist):
    plt.hist(hist, bins=256)
    plt.show()


if __name__ == "__main__":
    # read image
    # img = cv2.imread('images/mountain.jpeg', cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('original img', img)
    #
    # hist, t_hist = histogram(img)
    #
    # new_img = histogram_equalization(img, t_hist, 256)
    # cv2.imshow("histogram equalization", new_img)
    #
    # new_hist, new_t_hist = histogram(new_img)
    #
    # histogram_plot = draw_histogram(hist)
    # cv2.imshow("histogram plot", histogram_plot)
    #
    # histogram_plot_2 = draw_histogram(new_hist)
    # cv2.imshow("histogram plot_2", histogram_plot_2)
    #
    # draw_histogram_plt(hist)
    # draw_histogram_plt(new_hist)
    img = cv2.imread('images/mountain.jpeg')
    cv2.imshow('original img', img)
    b_channel = img[:,:,0]
    g_channel = img[:,:,1]
    r_channel = img[:,:,2]

    b_hist, b_t_hist = histogram(b_channel)
    g_hist, g_t_hist = histogram(g_channel)
    r_hist, r_t_hist = histogram(r_channel)

    new_b_channel = histogram_equalization(b_channel, b_t_hist, 256)
    new_g_channel = histogram_equalization(g_channel, g_t_hist, 256)
    new_r_channel = histogram_equalization(r_channel, r_t_hist, 256)

    new_img = img.copy()
    new_img[:,:,0] = new_b_channel
    new_img[:,:,1] = new_g_channel
    new_img[:,:,2] = new_r_channel

    # draw histogram plot
    b_histogram_plot = draw_histogram(b_hist, color=[255, 0, 0])
    cv2.imshow("b_histogram plot", b_histogram_plot)
    g_histogram_plot = draw_histogram(g_hist, color=[0, 255, 0])
    cv2.imshow("g_histogram plot", g_histogram_plot)
    r_histogram_plot = draw_histogram(r_hist, color=[0, 0, 255])
    cv2.imshow("r_histogram plot", r_histogram_plot)


    cv2.imshow("histogram equalization", new_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()