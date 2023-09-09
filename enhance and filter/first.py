import cv2
import numpy as np

img = cv2.imread("sample.jpg",0)
cv2.imshow("original image",img)
#contrast enhancement
#imgst = np.zeros(np.shape(img),dtype=np.uint8)
#cv2.normalize(img,imgst,0,255,cv2.NORM_MINMAX)
#cv2.imshow("stretched",imgst)
#
#hist = cv2.equalizeHist(img)
#cv2.imshow("histogram eq",hist)

# different filtering kernels
#bxblur= cv2.blur(img,(3,3))
#cv2.imshow('boxblur',bxblur)
#
#guss=cv2.GaussianBlur(img,(3,3),0)
#cv2.imshow('gauss',guss)
#
#sobel=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
#cv2.imshow('sobel',sobel)
#
#lap=cv2.Laplacian(img,cv2.CV_64F)
#cv2.imshow('laplace',lap)

#mblur=cv2.medianBlur(img,5)
#cv2.imshow('median',mblur)

#morphological operations
ret,binimg=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
dil=cv2.dilate(binimg,np.ones((3,3),dtype=np.uint8))
ero=cv2.erode(binimg,np.ones((3,3),dtype=np.uint8))

cv2.imshow("dilation",dil)
cv2.imshow("erosion",ero)
cv2.imshow("binary image",binimg)
 
cv2.waitKey(0)