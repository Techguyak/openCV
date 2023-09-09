import cv2
import numpy as np

img=cv2.imread("sample.jpg",0)
rows,cols = img.shape

trans = np.float32([[1,0,100],[0,1,50]])
rot = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)

dsrot=cv2.warpAffine(img,rot,(cols,rows))
dstrans=cv2.warpAffine(img,trans,(cols,rows))

cv2.imshow("Source Image" , img)
cv2.imshow( "Rotated Image" ,dsrot)
cv2.imshow("Translated Image", dstrans)

cv2.waitKey(0)