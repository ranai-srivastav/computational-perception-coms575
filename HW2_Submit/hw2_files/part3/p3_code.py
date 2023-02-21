# Write a program that uses basic morphological operations to identify and crop the 6x5 grid in the image shown
# below. The result image should contain only the pixels inside the grid (similar to the test images for the previous
# two problems).

import cv2

load_img = cv2.imread("image_part3b.png")
load_img = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)
_, load_img = cv2.threshold(load_img, 250, 255, cv2.THRESH_BINARY)
# load_img = load_img[60:550][:]
load_img = load_img

struct_elem = cv2.imread("6_5_Grid.png")
struct_elem = cv2.cvtColor(struct_elem, cv2.COLOR_BGR2GRAY)
_, struct_elem = cv2.threshold(struct_elem, 222, 255, cv2.THRESH_BINARY)

load_img = cv2.erode(~load_img, ~struct_elem)
load_img = cv2.dilate(load_img, struct_elem)

cv2.imshow("img", load_img)
cv2.waitKey(15000)

