import urllib3
import cv2
import numpy as np 
import ssl

url = "http://192.168.137.34:8080/video"
cap = cv2.VideoCapture(url)

while(cap.isOpened()):
    camera, frame = cap.read()
    try:
        cv2.imshow('Imagen',cv2.resize(frame,(600,400)))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    except cv2.error:
        print("end")
        break
cv2.destroyAllWindows()
