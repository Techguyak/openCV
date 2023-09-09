import cv2
import numpy as np

img = cv2.imread("sample.jpg",0)
ret,th= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
adap=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,20)
ret2,qust=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("global threshold",th)
cv2.imshow("adaptive",adap)
cv2.imshow("otsu",qust)

cv2.waitKey(0)