import cv2#libreria 
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

#tipos de letra
#FONT_HERSHEY_SIMPLEX = 0
#FONT_HERSHEY_PLAIN = 1
#FONT_HERSHEY_DUPLEX = 2
#FONT_HERSHEY_COMPLEX = 3
#FONT_HERSHEY_TRIPLEX = 4
#FONT_HERSHEY_COMPLEX_SMALL = 5
#FONT_HERSHEY_SCRIPT_SIMPLEX = 6
#FONT_HERSHEY_SCRIPT_COMPLEX = 7
