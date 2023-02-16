# 2. Find and mark all small squares in the empty grid. Change the color of the green squares to blue; and the color
# of the orange squares to brown. Solve this and all subsequent problems using either MATLAB or OpenCV.
import cv2
import numpy

load_img = cv2.imread("images/image_part2.png")
load_img = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)
load_img = ~load_img

load_struct_el = cv2.imread("images/Screenshot from 2023-02-14 00-12-33 .png")
load_struct_el = cv2.cvtColor(load_struct_el, cv2.COLOR_BGR2GRAY)
_, load_struct_el = cv2.threshold(load_struct_el, 250, 255, cv2.THRESH_BINARY)
load_struct_el = ~load_struct_el

load_img = cv2.erode(load_img, load_struct_el)
load_img = cv2.dilate(load_img, load_struct_el)

# _, grid = cv2.threshold(load_img, 39, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("raw", load_img)
cv2.waitKey(00)





