# Find and color all vowels within the grid (A, E, I, O, U, Y). Color each vowel in a different color.

import cv2
import numpy

INPUT_STRING = "image_part4a.png"

raw_img = cv2.imread(INPUT_STRING)
original = raw_img
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, raw_img = cv2.threshold(raw_img, 250, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
raw_img_inv = ~raw_img  # inverted has white bkg
