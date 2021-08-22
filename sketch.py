# Name-Arpan Das
# task-4 of LGM DATA-ANALYTICS of Beginner Task Level 1

import cv2
img_location="E:/"
filename="me2.jpg"
img=cv2.imread(img_location+filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invertimg=255-gray
blurimg=cv2.GaussianBlur(invertimg,(21,21),0)
invertedblur=255-blurimg
sketchpencil=cv2.divide(gray,invertedblur,scale=256.0 )
cv2.imshow("original image",img)
cv2.imshow("new image",sketchpencil)
cv2.waitKey(0)
