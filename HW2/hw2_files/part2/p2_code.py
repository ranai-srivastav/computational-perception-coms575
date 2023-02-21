# Find and mark all small squares in the grid. Change the color of the green squares to blue; and the color of the
# orange squares to brown. Solve this and all subsequent problems using either MATLAB or OpenCV.

import cv2
import numpy

load_img = cv2.imread("image_part2.png")
col_img = load_img

for i in range(len(col_img)):
    for j in range(len(col_img[i])):

        if col_img[i][j][0] < 200 and col_img[i][j][1] < 190 and col_img[i][j][2] < 120:  # Green to blue
            col_img[i][j] = numpy.array([212, 120, 100])

        if  80 < col_img[i][j][0] < 100 and \
            160 < col_img[i][j][1] < 190 and \
            190 < col_img[i][j][2] < 210:  # Yellow to brown
            col_img[i][j] = numpy.array([50, 87, 133])

cv2.imshow("Color modified", col_img)
# cv2.waitKey(5000)

load_img = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)
_, load_img = cv2.threshold(load_img, 250, 255, cv2.THRESH_BINARY)
load_img = ~load_img

load_struct_el = cv2.imread("Screenshot from 2023-02-14 00-12-33 .png")
load_struct_el = cv2.cvtColor(load_struct_el, cv2.COLOR_BGR2GRAY)
_, load_struct_el = cv2.threshold(load_struct_el, 250, 255, cv2.THRESH_BINARY)
load_struct_el = ~load_struct_el

load_img = cv2.erode(load_img, load_struct_el)
load_img = cv2.dilate(load_img, load_struct_el)

# _, grid = cv2.threshold(load_img, 39, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Squares", load_img)
cv2.waitKey(00)


