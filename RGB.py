#import cv2
#import numpy as np
#bgr = np.zeros((300, 300, 3), dtype=np.uint8)#Aquí es donde se
#está construyendo la imagen, con,zero es decir
#estamos creando una matriz de ceros, de 300 filas,
#300 columnas de 3 canales, correspondientes
#a BGR. Se especifica el tipo de dato con np.uint8,
#esto quiere decir que se tomará valores de entre 0 y 255.
#cv2.imshow('BGR', bgr)#Se realiza la visualización de la imagen, lo que mostraría
#bgr[:,:,:] = (255, 0, 100)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#Se puede modificar el color de la imagen creada
#añadiendo una línea en donde especifique las filas, columnas
#en donde se debe representar el nuevo color
import cv2
import numpy as np
bgr = np.zeros((300, 300, 3), dtype=np.uint8)
#bgr[:,:,:] = (20, 117, 240)#naranja
#bgr[:,:,:] = (255, 0, 0)#AZUL
#bgr[:,:,:] = (0, 255, 0)#verde
bgr[:,:,:] = (0, 0, 255)#rojo
bgr[:,:,:] = (109, 45, 212)#rosa
cv2.imshow('BGR', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
