import cv2
import numpy as np

img =cv2.imread("lena.jpg")
#sift
stimg = np.zeros(np.shape(img),dtype=np.uint8)
st = cv2.SIFT_create()
kp = st.detect(img,None)
siftimg=cv2.drawKeypoints ( img, kp, stimg)
#harris corner
ig = np.float32(img)
#dst =cv2.cornerHarris(ig,2,3,0.04)
Harrisimg=img.copy( )
Harrisimg=cv2.cvtColor(Harrisimg, cv2.COLOR_GRAY2BGR)
Harrisimg[dst>0.02*dst.max()] =[0,0,255]

cv2.imshow("sift",siftimg)
cv2.imshow("harris",Harrisimg)

cv2.waitKey(0)