import cv2
import numpy as np
import matplotlib.pyplot as plt

from imageutils import *
from mathutils import *


K = np.array([[1346.100595, 0, 932.1633975], 
              [0, 1355.933136, 654.8986796],	
              [0,	0, 	1]])

#testudo = cv2.imread('./testudo.png')
testudo=cv2.imread("C:\\Users\\pendl\\Downloads\\proj1\\proj1\\testudo.png")
h, w, _ = testudo.shape
testudo_corners = np.array([[0, 0], [h, 0], 
                            [h, w], [0, w],])

tag_dim = [160, 160]
tag_pts = np.array([[ 0, 0], [160, 0], 
                    [160, 160],[0, 160]])

cube_pos = np.array([[0,0,0,1],[0,160,0,1],[160,160,0,1],
                    [160,0,0,1],[0,0,-160,1],[0,160,-160,1],
                    [160,160,-160,1],[160,0,-160,1]])

sf = 4
i = 0
#cap = cv2.VideoCapture('./1tagvideo.mp4')
cap= cv2.VideoCapture("C:\\Users\\pendl\\Desktop\\ENPMP673\\Project1\\1tagvideo.mp4")
while cap.isOpened():
    ret, img = cap.read()
    if not ret: break
    img2 = img.copy()
    
    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
    gray_sf = cv2.resize(gray, (w//sf, h//sf))
    img_edge = edge_detection(gray_sf)
    
    cv2.imshow('edge', img_edge)
    tag_corners = corner_detection(img_edge)
    
    H = Homography(tag_corners*4, tag_pts)
    AR_tag = warpPerspective(gray, H, tag_dim)
    AR_tag = cv2.blur(AR_tag, (3, 3)) 
    AR_tag = threshold(AR_tag, 150)
    tag_id, tag_corners = decode_tag(AR_tag, tag_corners)
    
    print(tag_id)
    cv2.imshow('ARtag', AR_tag)
    
    tag_corners = tag_corners*sf
    H = Homography(tag_pts, tag_corners)
    
    H_inv = Homography(testudo_corners, tag_corners)
    warped_testudo = warpPerspective(testudo, H_inv, (w, h))
    
    cv2.fillConvexPoly(img, tag_corners, 0, 16)
    
    img = img + warped_testudo
    '''
    P = projectionMatrix(H, K)
    
    new_cube = P @ cube_pos.T
    new_cube = np.int0(new_cube[:2]/new_cube[2]).T
    
    img = draw_cube(img, new_cube)
    '''
    cv2.imshow('TestudoNCube', img)
    
    #cv2.imshow('img+testudo',img)
    if cv2.waitKey(10)&0xFF == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()