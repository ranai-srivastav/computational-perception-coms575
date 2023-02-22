# Find and color all vowels within the grid (A, E, I, O, U, Y). Color each vowel in a different color.

import cv2
import numpy

INPUT_STRING = "image_part5b.png"


def change_col(img, color):
    if INPUT_STRING == "image_part5a.png":
        for i in range(50, 240):
            for j in range(50, 400):
                if img[i][j][0] > 100 and img[i][j][1] > 100:
                    img[i][j] = color
    else:
        for i in range(50, 200):
            for j in range(50, 330):
                if img[i][j][0] > 100 and img[i][j][1] > 100:
                    img[i][j] = color
    return img


raw_img = cv2.imread(INPUT_STRING)
original = raw_img
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, raw_img = cv2.threshold(raw_img, 250, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
reset = raw_img
raw_img_inv = ~raw_img  # inverted has white bkg

# ---------------A----------------------- #
A_elem = cv2.imread("A.png")
A_elem = cv2.cvtColor(A_elem, cv2.COLOR_BGR2GRAY)
_, A_elem = cv2.threshold(A_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
A_elem_inv = ~A_elem  # has black bkg

# ---------------E----------------------- #
E_elem = cv2.imread("E.png")
E_elem = cv2.cvtColor(E_elem, cv2.COLOR_BGR2GRAY)
_, E_elem = cv2.threshold(E_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
E_elem_inv = ~E_elem  # has black bkg

# ---------------I----------------------- #
I_elem = cv2.imread("I.png")
I_elem = cv2.cvtColor(I_elem, cv2.COLOR_BGR2GRAY)
_, I_elem = cv2.threshold(I_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
I_elem_inv = ~I_elem  # has black bkg

# ---------------O----------------------- #
O_elem = cv2.imread("O.png")
O_elem = cv2.cvtColor(O_elem, cv2.COLOR_BGR2GRAY)
_, O_elem = cv2.threshold(O_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
O_elem_inv = ~O_elem  # has black bkg

# ---------------U----------------------- #
U_elem = cv2.imread("U.png")
U_elem = cv2.cvtColor(U_elem, cv2.COLOR_BGR2GRAY)
_, U_elem = cv2.threshold(U_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
U_elem_inv = ~U_elem  # has black bkg

# ---------------Y----------------------- #
Y_elem = cv2.imread("Y.png")
Y_elem = cv2.cvtColor(Y_elem, cv2.COLOR_BGR2GRAY)
_, Y_elem = cv2.threshold(Y_elem, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
Y_elem_inv = ~Y_elem  # has black bkg

# ------------------ MASKING --------------------

vert_mask = numpy.ones((40, 1), dtype=numpy.uint8)
# mask = numpy.ones((40, 1), dtype=numpy.uint8)
# vert_mask = numpy.hstack((vert_mask, mask))
_, vert_mask = cv2.threshold(vert_mask, 190, 255, cv2.THRESH_BINARY)
mask = cv2.erode(raw_img, ~vert_mask)
mask = ~mask
raw_img = cv2.bitwise_and(mask, raw_img)
raw_img = ~raw_img
# cv2.imshow("vert", raw_img)
# cv2.waitKey(10000)

# raw_img = reset
raw_img = cv2.erode(~raw_img, I_elem_inv)
I_elem_inv = cv2.flip(I_elem_inv, 0)
raw_img = cv2.dilate(raw_img, I_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([200, 100, 150]))
# cv2.imshow("I", col_mask)
fin_mask = col_mask

raw_img = reset
raw_img = cv2.erode(raw_img, A_elem_inv)
A_elem_inv = cv2.flip(A_elem_inv, 0)
raw_img = cv2.dilate(raw_img, A_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([200, 200, 10]))
# col_mask = cv2.bitwise_or(col_mask, original)
# cv2.imshow("A", col_mask)
fin_mask += col_mask

raw_img = reset
raw_img = cv2.erode(raw_img, E_elem_inv)
E_elem_inv = cv2.flip(E_elem_inv, 0)
raw_img = cv2.dilate(raw_img, E_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([100, 100, 100]))
# col_mask = cv2.bitwise_or(col_mask, original)
# cv2.imshow("E", col_mask)
fin_mask += col_mask

raw_img = reset
raw_img = cv2.erode(raw_img, O_elem_inv)
O_elem_inv = cv2.flip(O_elem_inv, 0)
raw_img = cv2.dilate(raw_img, O_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([100, 100, 10]))
# col_mask = cv2.bitwise_or(col_mask, original)
# cv2.imshow("O", col_mask)
fin_mask += col_mask

raw_img = reset
raw_img = cv2.erode(raw_img, U_elem_inv)
U_elem_inv = cv2.flip(U_elem_inv, 0)
raw_img = cv2.dilate(raw_img, U_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([30, 150, 200]))
# cv2.imshow("U", col_mask)
fin_mask += col_mask

raw_img = reset
raw_img = cv2.erode(raw_img, Y_elem_inv)
Y_elem_inv = cv2.flip(Y_elem_inv, 0)
raw_img = cv2.dilate(raw_img, Y_elem_inv)
col_mask = cv2.cvtColor(raw_img, cv2.COLOR_GRAY2BGR)
col_mask = change_col(col_mask, numpy.array([250, 150, 10]))
# cv2.imshow("Y", col_mask)
fin_mask += col_mask
cv2.imshow("final", fin_mask)

cv2.waitKey(10000)
