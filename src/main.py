import cv2 
import numpy as np 
 
cap = cv2.VideoCapture(0) 
logo = cv2.imread('sample_image.png') 
size = 100
logo = cv2.resize(logo, (size, size)) 
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) 
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY) 
  
while True: 
    ret, frame = cap.read() 
    roi = frame[-size-10:-10, -size-10:-10] 
    roi[np.where(mask)] = 0
    roi += logo 
    cv2.imshow('WebCam', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break
cap.release() 
cv2.destroyAllWindows() 
