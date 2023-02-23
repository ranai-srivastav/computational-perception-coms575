# This is the same as problem 8, but now also print two integers after each word that indicate the quality of the
# guess. The first integer indicates the number of letters in correct positions (green squares). The second integer
# maps to the correct letters but in wrong positions (orange squares). For example:
#
# CLOUD 1 1
#
# BLUNT 1 2
#
# ULTRA 5 0

import cv2
import numpy

letters = ["../../letter_cutouts/" + chr(char) + ".png" for char in range(65, 91)]
struct_elems = []

for letter in letters:
    letter_img = cv2.imread(letter)
    letter_img = cv2.cvtColor(letter_img, cv2.COLOR_BGR2GRAY)
    _, letter_img = cv2.threshold(letter_img, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    struct_elems.append(letter_img)


IMG_NAME = "image_part9b.png"

if IMG_NAME == "image_part9a.png":
    raw_img = cv2.imread(IMG_NAME)
    raw_img = raw_img[20:450, 40:400]
else:
    raw_img = cv2.imread(IMG_NAME)

bw_image = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, bw_image = cv2.threshold(bw_image, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("img", bw_image)
# cv2.waitKey(1000)

row_sum = numpy.sum(bw_image, axis=1, dtype=numpy.int64)

""" Breaking the image into rows """
row_edges = []
count = 0
last_elem = row_sum[0]
for offset, i in enumerate(row_sum):
    if abs(last_elem - i) > 70000:
        row_edges.append(offset)
    last_elem = i

rows = []
colored_rows = []

for i in range(len(row_edges)-1):
    img = bw_image[row_edges[i]:row_edges[i+1], :]
    col_row = raw_img[row_edges[i]:row_edges[i+1], :]
    i = i+2
    if count % 2 == 0:
        rows.append(img)
        colored_rows.append(col_row)
    count += 1

# for img in rows:
#     cv2.imshow("img", img)
#     cv2.waitKey(1000)

col_edges = []

col_sum = numpy.sum(rows[0], axis=0, dtype=numpy.int64)
last_elem = col_sum[0]
for offset, i in enumerate(col_sum):
    if abs(last_elem - i) > 8000:
        col_edges.append(offset)
    last_elem = i


"""Breaking each row into cols"""
for row, colored_row in zip(rows, colored_rows):
    cols = []
    colored_cols = []
    count = 0
    for i in range(len(col_edges)-1):
        img = row[:, col_edges[i]:col_edges[i+1]]
        rangeen = colored_row[:, col_edges[i]:col_edges[i+1]]

        i = i+2
        if count % 2 == 0:
            cols.append(img)
            colored_cols.append(rangeen)
        count += 1

    letter_masks = []
    detected_letters = []

    num_green = 0
    num_yellow = 0

    for colored_col in colored_cols:
        green = cv2.cvtColor(colored_col, cv2.COLOR_BGR2HSV)
        lower = numpy.array([55, 10, 10])
        upper = numpy.array([65, 255, 255])
        green = cv2.inRange(green, lower, upper)

        if numpy.any(green):
            num_green += 1
            continue

        yellow = cv2.cvtColor(colored_col, cv2.COLOR_BGR2HSV)
        lower = numpy.array([23, 60, 80])
        upper = numpy.array([28, 255, 255])
        yellow = cv2.inRange(yellow, lower, upper)

        if numpy.any(yellow):
            num_yellow += 1
            continue

    for img in cols:
        # cv2.imshow("actual", img)
        # cv2.waitKey(500)
        is_E = False
        for i, se in enumerate(struct_elems):
            mask = cv2.erode(img, ~se)
            mask = mask[:-9]
            se = cv2.flip(se, 0)
            se = cv2.flip(se, 1)
            mask = cv2.dilate(mask, ~se)
            # cv2.imshow("mask", mask)
            # cv2.waitKey(100)
            # letter_masks.append(mask)

            if numpy.any(mask) and (i % 26) != 5 and (i % 26) != 8:
                # cv2.imshow(f"detected {i % 26}", mask)
                if i == 4:
                    is_E = True
                if is_E and i == 11:
                    continue
                print(chr((i % 26) + 65), end=" ")
    print("", end="  ")
    print(num_green, end=" ")
    print(num_yellow, end=" ")

    print()

