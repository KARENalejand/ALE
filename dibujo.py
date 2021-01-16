import cv2
import numpy as np

imagen = 255*np.ones((400,600,3),dtype=np.uint8)##crea una imagen en blanco
#crear lineas
cv2.line(imagen,(0,0),(600,400),(255,0,0),4)
#cordenadas x y y    0iicio final 600 color de la ninea 4 es el  grosor de lalinea
#DIBUJAR UN RECTANGULO
cv2.rectangle(imagen,(50,80),(200,200),(0,255,0),3)
            #coordenadas         #Tamaño #color
#dibuar uncirculo
cv2.circle(imagen,(300,200),100,(0,0,0),3)
                    #cordenada#radio #color -1 para estar lleno


#para visualizar texto se utilizan ls siguentes comandos
font = cv2.FONT_HERSHEY_SIMPLEX
                #fuente
cv2.putText(imagen,'colores',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)

                      #posicion#  #fuente de letra#COLOR#GROSOR

cv2.imshow('imagen',imagen)#visualiza la imgen
cv2.waitKey(0)#presinar cualquier tecla para  dejar de fumcionar 
cv2.destroyAllWindows()##cerrar la ventanas
##para dibujar una linea utilizamos


