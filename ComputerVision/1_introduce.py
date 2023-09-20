from pprint import pprint

import cv2
import numpy as np

# read images
img = cv2.imread('images/demo.jpeg')


rows, cols, channels = img.shape
print(f"{rows=}, {cols=}, {channels=}")

# T shape
delta = 50
for i in range(delta, rows-delta):
    for j in range(cols//2 - delta, cols//2 + delta):
        img[i][j] = [0, 255, 0] # B, G, R

for i in range(delta, 3*delta):
    for j in range(delta*2, cols-2*delta):
        img[i][j] = [0, 255, 0] # B, G, R

cv2.imshow("Demo img", img)


# 2 shapes

img2 = cv2.imread('images/demo.jpeg')

delta = 80
# create numpy bitmask
mask = np.ones(img2.shape[:2], dtype=np.uint8)
for i in range(delta, rows-delta):
    for j in range(delta, cols-delta):
        mask[i][j] = 0

delta = 50
for i in range(rows//2 - delta, rows//2 + delta):
    for j in range(cols//2 - delta, cols//2 + delta):
        mask[i][j] = 1

print(mask)
img2_masked = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow("Demo img2 masked", img2_masked)

img3 = cv2.imread('images/demo.jpeg')

radius1 = 40
radius2 = 2*radius1
mask2 = np.ones(img3.shape[:2], dtype=np.uint8)
for i in range(rows):
    for j in range(cols):
        if (i - rows//2)**2 + (j - cols//2)**2 < radius2**2:
            mask2[i][j] = 0

        if (i - rows//2)**2 + (j - cols//2)**2 <= radius1**2:
            mask2[i][j] = 1

pprint(mask2)
img3_masked = cv2.bitwise_and(img3, img3, mask=mask2)
cv2.imshow("Demo img3 donut", img3_masked)

gray_img = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
cv2.imshow("Demo gray img", gray_img)

cv2.waitKey(33)
cv2.destroyAllWindows()
