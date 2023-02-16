# 4. Find all 'A' letters within the grid and color them red.

import cv2
import numpy

raw_img = cv2.imread("images/image_part4a.png")
# raw_img = cv2.blur(raw_img, (2, 2))
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, raw_img = cv2.threshold(raw_img, 250, 255, cv2.THRESH_BINARY)
raw_img = ~raw_img  # inverted has white bkg

# cv2.imshow("img", raw_img)
# cv2.waitKey(3000)

struct_elem = cv2.imread("images/letter_cutouts/A.png")
struct_elem = cv2.cvtColor(struct_elem, cv2.COLOR_BGR2GRAY)
_, struct_elem = cv2.threshold(struct_elem, 225, 255, cv2.THRESH_BINARY)
# struct_elem = ~struct_elem  # has black bkg

rm_noise = numpy.zeros((3, 3), dtype=numpy.uint8)
rm_noise[1][1] = 254
_, rm_noise = cv2.threshold(rm_noise, 215, 255, cv2.THRESH_BINARY)

# for i in range(len(raw_img)):
#     for j in range(len(raw_img[i])):
#         print(f'{raw_img[i][j]:3}', end=" ")
#     print(" ")

# cv2.imshow("struct elem", struct_elem)
# cv2.waitKey(3000)
#
raw_img = cv2.erode(raw_img, struct_elem)
raw_img = cv2.erode(raw_img, rm_noise)

# struct_elem = cv2.flip(struct_elem, 0)
# raw_img = cv2.dilate(raw_img, struct_elem)

# raw_img = cv2.morphologyEx(raw_img, cv2.MORPH_OPEN,
#                            struct_elem, iterations=2)


cv2.imshow("img", raw_img)
cv2.waitKey(000)

