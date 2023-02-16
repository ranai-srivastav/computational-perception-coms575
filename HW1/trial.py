import cv2
import numpy

rm_noise = numpy.zeros((3, 3), dtype=numpy.uint8)
rm_noise[1][1] = 254
_, rm_noise = cv2.threshold(rm_noise, 215, 255, cv2.THRESH_BINARY)
