# Write a program that uses basic morphological operations to identify and crop the 6x5 grid in the image shown
# below. The result image should contain only the pixels inside the grid (similar to the test images for the previous
# two problems).

import cv2
import numpy

load_img = cv2.imread("image_part3b.png")
load_img = cv2.cvtColor(load_img, cv2.COLOR_BGR2GRAY)
_, load_img = cv2.threshold(load_img, 250, 255, cv2.THRESH_BINARY)
# load_img = load_img[60:550, :]
load_img = load_img

struct_elem = cv2.imread("6_5_Grid.png")
struct_elem = cv2.cvtColor(struct_elem, cv2.COLOR_BGR2GRAY)
_, struct_elem = cv2.threshold(struct_elem, 222, 255, cv2.THRESH_BINARY)

load_img = cv2.erode(~load_img, ~struct_elem)
load_img = cv2.dilate(load_img, struct_elem)

row_sum = numpy.sum(load_img, 1, dtype=numpy.int64)
col_sum = numpy.sum(load_img, 0, dtype=numpy.int64)

bot_edge = 454
top_edge = 144
left_edge = 570
right_edge = 826

for row, val in enumerate(row_sum):
    if val > 0:
        top_edge = row
        break
    prev = val

row_sum = numpy.flip(row_sum)

prev = row_sum[0]
for row, val in enumerate(row_sum):
    if val > 0:
        bot_edge = row
        break
    prev = val

prev = col_sum[0]
for col, val in enumerate(col_sum):
    if val > 0:
        left_edge = col
        break
    prev = col

col_sum = numpy.flip(col_sum)
prev = col_sum[0]
for col, val in enumerate(col_sum):
    if val > 0:
        right_edge = col
        break
    prev = col

bot_edge = 454
top_edge = 144
left_edge = 570
right_edge = 826

print(bot_edge)
print(top_edge)
print(left_edge)
print(right_edge)

load_img = load_img[top_edge:bot_edge, left_edge:right_edge]


cv2.imwrite("solution_part3.png", load_img)
# cv2.waitKey(000)

