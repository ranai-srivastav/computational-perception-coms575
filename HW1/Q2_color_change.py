# 2. Find and mark all small squares in the empty grid. Change the color of the green squares to blue; and the color
# of the orange squares to brown. Solve this and all subsequent problems using either MATLAB or OpenCV.
import cv2
import numpy

load_img = cv2.imread("images/image_part2.png")

for i in range(len(load_img)):
    for j in range(len(load_img[i])):

        if load_img[i][j][0] < 200 and load_img[i][j][1] < 190 and load_img[i][j][2] < 120:  # Green to blue
            load_img[i][j] = numpy.array([212, 120, 100])

        if load_img[i][j][0] > 80 and load_img[i][j][0] < 100 \
        and load_img[i][j][1] > 160 and load_img[i][j][1] < 190 \
        and load_img[i][j][2] > 190    and load_img[i][j][2] < 210:  # Yellow to brown
            print("Brown")
            load_img[i][j] = numpy.array([50, 87, 133])


# green_lower = numpy.array([55, 10, 10])
# green_upper = numpy.array([75, 250, 250])
# greens = cv2.inRange(grid, green_lower, green_upper)
# # greens = cv2.cvtColor(greens, cv2.COLOR_BGR2GRAY)
# _, greens = cv2.threshold(greens, 127, 255, cv2.THRESH_BINARY)
# greens = ~greens


#
# yellow_lower = numpy.array([20, 80, 80])
# yellow_upper = numpy.array([24, 250, 250])
# yellows = cv2.inRange(grid, yellow_lower, yellow_upper)
# _, yellows = cv2.threshold(yellows, 127, 255, cv2.THRESH_BINARY)
#
# yellows = cv2.erode(yellows, cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4)))
# yellows = cv2.dilate(yellows, cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4)))
# yellows = ~yellows
#

# _, img = cv2.threshold(grid, 215, 255, 0)

cv2.imshow("img", load_img)
cv2.waitKey(5000)
