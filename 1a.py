import cv2
import numpy as np
import matplotlib.pyplot as plt

from imageutils import *
from mathutils import *
count =0
sf = 4
#####change the path below #######
cap= cv2.VideoCapture("C:\\Users\\pendl\\Downloads\\proj1\\proj1\\1tagvideo.mp4")
while cap.isOpened():
    ret, img = cap.read()
    if not ret: break
    

    if count==0:
        image= img.copy()
        img2 = img.copy()
    
        h, w, _ = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
        gray_sf = cv2.resize(gray, (w//sf, h//sf))
        img_edge = edge_detection(gray_sf)
    
        cv2.imshow('edge', img_edge)
        tag_corners = corner_detection(img_edge)
        tag_corners = np.int0(tag_corners)

        print(tag_corners)

    # Iterate over the corners and draw a circle at that location
        for i in tag_corners:
            x,y = i.ravel()
            cv2.circle(gray_sf,(x,y),5,(0,0,255),-1)
    
    # Display the image
        cv2.imshow('a',gray_sf)
        cv2.waitKey(0)
    count +=1    

    if cv2.waitKey(10)&0xFF == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()