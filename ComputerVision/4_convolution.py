import cv2
import numpy as np
from numba import njit, jit

@jit(forceobj=True)
def convolution(img, kernel):
    new_img = img.copy()
    H = kernel.shape[0] // 2
    W = kernel.shape[1] // 2
    for i in range(H, img.shape[0] - H):
        for j in range(W, img.shape[1] - W):
            tmp = 0
            for dx in range(-H, H+1):
                for dy in range(-W, W+1):
                    tmp += kernel[H+dx,W+dy] * img[i+dx, j+dy]
            new_img[i,j] = max(0, tmp)
    # return verify_image(new_img)
    return new_img

def verify_image(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = int(img[i][j])
            img[i][j] = max(0, min(img[i][j], 255))
    return img

def class_exercise(kernel):
    I = np.matrix([[1, 2, 4, 5, 8, 7], [2, 31, 1, 4, 2, 2], [4, 5, 5, 8, 8, 2], [1, 2, 1, 1, 4, 4], [7, 2, 2, 1, 5, 2]],
                  dtype=np.uint8)

    convoluted_image = convolution(I, kernel)
    cv2.imshow("original img", np.uint8(I))
    cv2.imshow("convoluted img", np.uint8(convoluted_image))

def real_image(kernel):
    # img = cv2.imread("images/egypt.jpeg", cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("images/demo.jpeg", cv2.IMREAD_GRAYSCALE)
    convoluted_image = convolution(img, kernel)
    cv2.imshow("original img", img)
    cv2.imshow("convoluted img", convoluted_image)


if __name__ == "__main__":
    kernel = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float16) * 1 / 9
    kernel2 = np.diag(np.ones(5), 0) * 1/25
    kernel3 = np.diag(np.ones(7), 0) * 1 / 45
    kernel4 = np.ones((5,5)) * 1/25
    kernel5 = np.ones((7,7,)) * 1 / 45

    kernel6 = np.matrix([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float16)
    kernel7 = np.ones((3,3)) * -1
    kernel7[1, 1] = 9
    kernel8 = np.ones((5,5)) * -1
    kernel8[2,2] = 25
    # class_exercise(kernel2)
    real_image(kernel8)
    print(kernel8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
