"""
Simple script for obstacle avoidance - vision in python
"""

import time
import numpy as np
import cv2

rawImage = cv2.imread('contours.jpg', 0)
cv2.imshow("image", rawImage)
cv2.waitKey(0)


def searchForMovement(image, rawImage):
    objectDetected = False

    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# if contours vector is not empty, we have found some objects
    if len(contours) != 0:
        objectDetected = True
        #cnt = contours[0]
        cnt = max(contours, key=cv2.contourArea)
        M = cv2.moments(cnt)
        print M
        # centroid of the contour
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print cx, cy
        # for adding a green ellipse
        rgbImage = cv2.cvtColor(rawImage, cv2.COLOR_GRAY2BGR)
        # draw an ellipse out of the contour points
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(rgbImage, ellipse, (0, 255, 0), 2)

        cv2.imshow("Result", rgbImage)
        cv2.waitKey(0)
    else:
        objectDetected = False


def main():
    ret, imageThresh = cv2.threshold(rawImage, 150, 255, 0)
    cv2.imshow("imageThresh", imageThresh)
    cv2.waitKey(0)
    searchForMovement(imageThresh, rawImage)


main()



