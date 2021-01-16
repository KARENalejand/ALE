import cv2
captura=cv2.VideoCapture(0)

while(captura.is()):
       
    ret,imagen=captura.read()
    if ret==True:
    
        cv2.imshow('Video',imagen)
        if cv2.waitKey(1)&0xFF== ord('s'):###finalizar la cara
            break
    
    captura.release()
    cv2.destroyAllWinows()
    
