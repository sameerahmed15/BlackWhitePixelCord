from cv2 import cv2
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from PIL import Image

coordinates=np.zeros((1,2),np.int)
counter=0


def mousePoints(event, x, y, flags, params):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        coordinates[counter]=x,y
        print(coordinates)

original=cv2.imread('original.png')     #path to original image
img=cv2.imread('finalThresh.png')       #path to segmented image

image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

contours, heirarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

size=len(contours)

for i in contours:
    area=cv2.contourArea(i)
    cv2.drawContours(img, [i], -1,(0,255,0),2)

#saving coordinates in txt file 
img1=Image.open('finalThresh.png')
sze=w,h=img1.size
data=img1.load()

pieces=[]
blackPix=[]
whitePix=[]

for x in range(w):
    for y in range(h): 
        color=data[x,y]
        if color==0:
            blackPix.append((x, y, color))
            
        elif color==255:
            whitePix.append((x, y, color))
#print (pieces)

# saving list of pixels in a text file

# coordinates in the segmented image that are black in color (brash/noise) 
with open('blackPix.txt','w') as handle:
    for i in blackPix:
        handle.write(str(i))

# coordinates in the image that are white in color (ice)
with open('whitePix.txt','w') as handle:
    for j in whitePix:
        handle.write(str(j))


cv2.imshow('image', img)
cv2.imshow('original', original)

cv2.waitKey(0)
cv2.destroyAllWindows