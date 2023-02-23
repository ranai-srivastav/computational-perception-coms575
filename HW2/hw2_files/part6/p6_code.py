# Find all vowels within the grid and replace each with the same letter but in a different font.
#
# You will have to make your own templates for the new versions of the six vowels, or figure out some other way to
# print text to an image at the right pixel coordinates. Cutouts of all symbols used in this problem can be found in
# the letter_cutouts folder.

import cv2
import numpy

IMG_NAME = "image_part6a.png"

letters = ["../../letter_cutouts/" + chr(char) + ".png" for char in range(65, 91)]
struct_elems = []

for letter in letters:
    letter_img = cv2.imread(letter)
    letter_img = cv2.cvtColor(letter_img, cv2.COLOR_BGR2GRAY)
    _, letter_img = cv2.threshold(letter_img, 225, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    struct_elems.append(letter_img)

paths = [x + "_replacement.png" for x in ["A", "E", "I", "O", "U"]]
replacements = []

for i, path in enumerate(paths):
    letter_img = cv2.imread(path)
    letter_img = cv2.cvtColor(letter_img, cv2.COLOR_BGR2GRAY)
    _, letter_img = cv2.threshold(letter_img, 220, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if i == 0:
        letter_img = ~letter_img
        letter_img = letter_img[5:-10, 15:-20]
    elif i == 1:
        letter_img = letter_img[10:, :-25]
    elif i == 2:
        letter_img = letter_img[20:, 20:-20]
    elif i == 3:
        letter_img = letter_img[:-10, 5:-10]
    elif i == 4:
        letter_img = letter_img[20:-10, 20:-20]
        letter_img = cv2.resize(letter_img, (int(letter_img.shape[0]*0.6), int(letter_img.shape[1]*0.6)))
    replacements.append(letter_img)
    # cv2.imshow("Final img", letter_img)
    # cv2.waitKey(0000)

if IMG_NAME == "image_part6a.png":
    raw_img = cv2.imread(IMG_NAME)
    raw_img = raw_img[20:450, 40:400]
else:
    raw_img = cv2.imread(IMG_NAME)

bw_image = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, bw_image = cv2.threshold(bw_image, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

col_sum = numpy.sum(bw_image, axis=0)
row_sum = numpy.sum(bw_image, axis=1)

last_elem = row_sum[-1]
for offset, i in enumerate(numpy.flip(row_sum)):
    if last_elem > i:
        break
    else:
        last_elem = i

bw_image = bw_image[:offset, :]

vert_se = numpy.ones((int(bw_image.shape[0] * 0.75), 1), dtype=numpy.uint8) * 151
_, vert_se = cv2.threshold(vert_se, 200, 255, cv2.THRESH_BINARY)

hor_se = numpy.ones((1, int(bw_image.shape[1] * 0.75)), dtype=numpy.uint8) * 151
_, hor_se = cv2.threshold(hor_se, 200, 255, cv2.THRESH_BINARY)

vert_mask = cv2.erode(bw_image, ~vert_se)
hor_mask = cv2.erode(bw_image, ~hor_se)
bw_image = cv2.bitwise_and(bw_image, ~vert_mask)
bw_image = cv2.bitwise_and(bw_image, ~hor_mask)
# cv2.imshow("mask", bw_image)

# R and B have an F
# B, D, E, F, H, K,  L,  M,  N,  P,  R,  T, all have an
# 1, 3, 4, 5, 7, 10, 11, 12, 13, 15, 17, 19


detected_letters = []
letter_masks = []

for i, se in enumerate(struct_elems):
    mask_in = cv2.erode(bw_image, ~se)
    mask_out = cv2.erode(~bw_image, se)
    se = cv2.flip(se, 0)
    se = cv2.flip(se, 1)
    mask = cv2.bitwise_and(~mask_out, mask_in)
    if i == 0:
        se = ~replacements[0]
        se = cv2.flip(se, 0)
        se = numpy.flip(se, 1)
        mask = cv2.dilate(mask, se)
    elif i == 4:
        se = ~replacements[1]
        se = cv2.flip(se, 0)
        se = numpy.flip(se, 1)
        mask = cv2.dilate(mask, se)
    elif i == 8:
        se = ~replacements[2]
        se = cv2.flip(se, 0)
        se = numpy.flip(se, 1)
        mask = cv2.dilate(mask, se)
    elif i == 14:
        se = ~replacements[3]
        se = cv2.flip(se, 0)
        se = numpy.flip(se, 1)
        mask = cv2.dilate(mask, se)
    elif i == 20:
        se = ~replacements[4]
        se = cv2.flip(se, 0)
        se = numpy.flip(se, 1)
        mask = cv2.dilate(mask, se)
    else:
        mask = cv2.dilate(mask, ~se)
    letter_masks.append(mask)

for i, mask in enumerate(letter_masks):

    if i == 5:
        mask = cv2.bitwise_and(mask, ~letter_masks[1])
        mask = cv2.bitwise_and(mask, ~letter_masks[17])

    if i == 8:
        # cv2.imshow("pre dIlate", mask)
        se = numpy.ones((23, 3), dtype=numpy.uint8) * 201
        _, se = cv2.threshold(se, 200, 255, cv2.THRESH_BINARY)
        mask = cv2.erode(mask, se)
        # cv2.imshow("dilate", mask)
        mask = cv2.bitwise_and(mask, ~letter_masks[1])
        mask = cv2.bitwise_and(mask, ~letter_masks[3])
        mask = cv2.bitwise_and(mask, ~letter_masks[4])
        mask = cv2.bitwise_and(mask, ~letter_masks[5])
        mask = cv2.bitwise_and(mask, ~letter_masks[7])
        mask = cv2.bitwise_and(mask, ~letter_masks[11])
        mask = cv2.bitwise_and(mask, ~letter_masks[12])
        mask = cv2.bitwise_and(mask, ~letter_masks[13])
        mask = cv2.bitwise_and(mask, ~letter_masks[15])
        mask = cv2.bitwise_and(mask, ~letter_masks[17])
        mask = cv2.bitwise_and(mask, ~letter_masks[19])
        mask = cv2.dilate(mask, ~struct_elems[8])
        # cv2.imshow("I w/o repeat", mask)

    if numpy.any(mask):
        detected_letters.append(mask)

fin_img = detected_letters[0]

for mask in detected_letters:
    fin_img += mask

# for mask in detected_letters:
#     color = numpy.array([numpy.random.randint(0, 255), numpy.random.randint(0, 255), numpy.random.randint(0, 255)])
#     for i, row in enumerate(mask):
#         for j, pxl in enumerate(row):
#             if pxl > 200:
#                 raw_img[i][j] = color

cv2.imshow("Final img", fin_img)
cv2.imwrite("p6_answer.png", fin_img)
cv2.waitKey(0000)
