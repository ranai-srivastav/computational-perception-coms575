# Solve at least two Wordle puzzles by playing the game online (Wordle).
# Take screenshots of the browser window as you play the game (after each guess).
# Then, run these images through your program. This is essentially the same as problem 9,
# but with images that you generated. Make sure to match the scale (or image resolution)
# in order to use the same letter templates. Note: For this problem, you may have to create
# your own letter templates by cropping them from the new test images using your favorite image editor.

import cv2
import numpy

letters = [
    "A10.png",
    "E10.png",
    "G10.png",
    "H10.png",
    "O10.png",
    "R10.png",
    "S10.png",
    "T10.png",
    "U10.png",
    "V10.png",
]

list_of_letters = ["A", "E", "G", "H", "O", "R", "S", "T", "U", "V"]
struct_elems = []

er = numpy.array([0, 150, 150, 150, 0], dtype=numpy.uint8).reshape(1, -1)
_, er = cv2.threshold(er, 100, 255, cv2.THRESH_BINARY)

for i, letter in enumerate(letters):
    letter_img = cv2.imread(letter)
    letter_img = cv2.cvtColor(letter_img, cv2.COLOR_BGR2GRAY)
    _, letter_img = cv2.threshold(letter_img, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if letter == "R10.png" and i == 5:
        letter_img = cv2.erode(letter_img, er)

    cv2.imshow("se", letter_img)
    cv2.waitKey(00)
    struct_elems.append(letter_img)

IMG_NAME = "image_part10.png"

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
            se = cv2.erode(se, er)
            mask = cv2.erode(img, se)
            mask = mask[:-9]
            se = cv2.flip(se, 0)
            se = cv2.flip(se, 1)
            mask = cv2.dilate(mask, ~se)
            # letter_masks.append(mask)

            if numpy.any(mask):
                print(list_of_letters[i], end=" ")
    print("", end="  ")
    print(num_green, end=" ")
    print(num_yellow, end=" ")

    print(" ")

