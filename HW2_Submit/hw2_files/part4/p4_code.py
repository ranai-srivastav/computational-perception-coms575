# 4. Find all 'A' letters within the grid and color them red.

import cv2
import numpy

INPUT_STRING = "image_part4a.png"

raw_img = cv2.imread(INPUT_STRING)
original = raw_img
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, raw_img = cv2.threshold(raw_img, 250, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
raw_img_inv = ~raw_img  # inverted has white bkg

struct_elem = cv2.imread("A.png")
struct_elem = cv2.cvtColor(struct_elem, cv2.COLOR_BGR2GRAY)
_, struct_elem = cv2.threshold(struct_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
struct_elem_inv = ~struct_elem  # has black bkg

red_mask = cv2.erode(raw_img, struct_elem_inv)
struct_elem_inv = cv2.flip(struct_elem_inv, 0)
red_mask = cv2.dilate(red_mask, struct_elem_inv)

fin_img = cv2.cvtColor(red_mask, cv2.COLOR_GRAY2BGR)

if INPUT_STRING == "image_part4a.png":
    row_mask = (45, 232)
    col_mask = (70, 390)
else:
    row_mask = (0, 200)
    col_mask = (13, 340)


# for i in range(40, 235):
for i in range(row_mask[0], row_mask[1]):
    # for j in range(65, 390):
    for j in range(col_mask[0], col_mask[1]):
        if fin_img[i][j][0] > 200 and fin_img[i][j][1] > 200:
            original[i][j] = numpy.array([0, 0, 255])

cv2.imshow("All As", original)
cv2.waitKey(8000)
