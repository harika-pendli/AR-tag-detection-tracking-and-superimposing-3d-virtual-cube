import cv2
import numpy as np
import matplotlib.pyplot as plt

from imageutils import *
from mathutils import *

image=cv2.imread("C:\\Users\\pendl\\Downloads\\proj1\\proj1\\ref_tag.jpeg")
dim = (160, 160)
# resize image
AR_tag = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
AR_tag = cv2.blur(AR_tag, (3, 3)) 
AR_tag = threshold(AR_tag, 150)
tag_corners=np.array([[0,0],[0,159],[159,159],[159,0]])
#print(tag_corners.shape)
tag_id, tag_corners = decode_tag(AR_tag, tag_corners)

print("tag_id :",tag_id)
cv2.imshow('ARtag', AR_tag)
cv2.waitKey(0)
tag_value=0
count=0
tot=0
for i in tag_id:
    tot= tot+int(i)*pow(2,(3-count))
    count+=1
print("tag_value", tot)

