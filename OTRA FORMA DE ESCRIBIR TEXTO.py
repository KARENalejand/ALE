import cv2
import numpy as np# LIBRERIAS 
imagen = 255*np.ones((400,600,3),dtype=np.uint8)
cv2.putText(imagen,'Practicando con OpenCV',(10,30),0,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,60),1,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,90),2,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,120),3,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,150),4,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,180),5,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,210),6,1,(255,0,0),2)
cv2.putText(imagen,'Practicando con OpenCV',(10,240),7,1,(255,0,0),2)

#cv2.putText# LIBRERIA PARA ESCRIBIR TEXTO


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
