import cv2
import numpy as np

img = cv2.imread("sample.jpg",1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow("hsv",hsv)
cv2.imshow("grey",gry)
cv2.imshow("ycrcb",ycrcb)



cv2.waitKey(0)