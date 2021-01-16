import cv2###libreria
import numpy as np##libreia
cap = cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  if ret==True:
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()
