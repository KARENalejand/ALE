import numpy as np ##para trabajar con marices
import cv2
img=cv2.imread('h.png',0) ##0 conviete a grises
cv2.imshow('imagen',img)###cargar imagen
k=cv2.waitKey(0)##sirve para cerrar la imagen
##cv2.imwrite('j.png',img)##guardar imagen
if k==27:
    cv2.destroyAllWindows() #detruir

elif k== ord('o'):
    cv2.imwrite('j.png',img) ##guardar imagen
    cv2.destroyAllWindows() #detruir
    
