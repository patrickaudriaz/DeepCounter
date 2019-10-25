#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import numpy as np

os.sys.path

import cv2

counter = 0


# In[2]:


video = cv2.VideoCapture(0)

height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)

# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier('../../Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX


# In[3]:


while(True):
    # Capture frame-by-frame
    ret, frame = video.read()
    
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    coord = str(faces)
    
    fps = str(video.get(cv2.CAP_PROP_FPS))
    
    cv2.putText(frame, coord, (0,20), font, 0.7, (0,255,0), 1, cv2.LINE_AA)
    cv2.putText(frame, fps, (0,50), font, 0.7, (0,255,0), 1, cv2.LINE_AA)
    
    cv2.line(frame,(int(width/3), 0),(int(width/3),int(height)),(0,0,255),2)
    cv2.line(frame,(int(width/3*2), 0),(int(width/3*2),int(height)),(255,0,255),2)


    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
# When everything done, release the capture
video.release()
cv2.destroyAllWindows()

