import cv2
import numpy as np

#Cargamos el clasificador con extensión xml con ayuda de cv2.CascadeClassifier, dentro
#entre comillas especificamos el nombre y extensión del archivo
#faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")#rostro
faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")#ojos
#i=cv2.imread('rostro.jpeg')#carga laimagen
i=cv2.imread('cat.jpeg')#carga laimagen

faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")#ojos

gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)#la transformamos a escala de grises

#es necesario aplicarlo en la imagen, para ello utilizaremos
#detectMultiScale que debe
#estar seguido de la variable con la cual se asignó la carga del clasificador
faces = faceClassif.detectMultiScale(gray,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(30,30),
  maxSize=(200,200))

for (x,y,w,h) in faces: # si s detecta el rostro se dan medidas
  cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)# dibuja unrectangulo en el rostro que se va a detectar



cv2.imshow('rostro',i)#vizualiza laimagen
cv2.waitKey(0)


