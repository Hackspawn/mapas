import cv2 #esto importa opencv
import numpy as np

cap = cv2.VideoCapture(0) #captura de video puedo reemplazarlo el (0) por ('video.mp4')
#img = cv2.imread('img.jpg') #para abrir imagenes

while True:
    ret, frame = cap.read() # captura el primer frame de video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cambia modo de color RGB a Gris
    mapa = cv2.applyColorMap(gray, cv2.COLORMAP_JET) #aplica mapa de color (JET)
    blur = cv2.blur(gray, (4,4)) #esto aplica un desenfoque
    edge = cv2.Canny(blur, 10, 100) # dibuja contornos de imagen desenfocada
    dst = cv2.bitwise_not(edge) #invierte los colores del dibujo
    
    
    #cv2.imshow('ventana', frame)
    #cv2.imshow('ventana_2', gray)
    cv2.imshow('ventana_3', mapa)
    cv2.imshow('ventana_4', blur)
    cv2.imshow('ventana_5', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.imwrite('mapa_2.jpg', mapa) #guarda un jpg del mapa de color
cv2.imwrite('dibujo_2.jpg', dst) #guarda un jpg del dibujo

