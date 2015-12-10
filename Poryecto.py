import numpy as np
import cv2
 
def funcion(x):
    pass
# se crean una variable camara y se coloca disponible.

cap = cv2.VideoCapture(0)
cv2.namedWindow('configuracion')
cv2.namedWindow('configuracion imagen') 
# Crearemos los controles para los colores.
 
cv2.createTrackbar ('H minimo', 'configuracion', 0,255,funcion)
cv2.createTrackbar ('H maximo', 'configuracion', 0,255,funcion)
cv2.createTrackbar ('S minimo', 'configuracion', 0,255,funcion)
cv2.createTrackbar ('S maximo', 'configuracion', 0,255,funcion)
cv2.createTrackbar ('V minimo', 'configuracion', 0,255,funcion)
cv2.createTrackbar ('V maximo', 'configuracion', 0,255,funcion)

cv2.createTrackbar ('H minimo', 'configuracion imagen', 0,255,funcion)
cv2.createTrackbar ('H maximo', 'configuracion imagen', 0,255,funcion)
cv2.createTrackbar ('S minimo', 'configuracion imagen', 0,255,funcion)
cv2.createTrackbar ('S maximo', 'configuracion imagen', 0,255,funcion)
cv2.createTrackbar ('V minimo', 'configuracion imagen', 0,255,funcion)
cv2.createTrackbar ('V maximo', 'configuracion imagen', 0,255,funcion)
 

 
# Iniciamos el ciclo de captura.

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #captura la imagen de la camara y la pasamos a HSV y se guarda en la variable declarada
    hsb = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
     
     
    # Asignamos las variables del rango de color que seguiremos
    
    Hminimo = cv2.getTrackbarPos('H minimo', 'configuracion')
    Hmaximo = cv2.getTrackbarPos('H maximo', 'configuracion')
    Sminimo = cv2.getTrackbarPos('S minimo', 'configuracion')
    Smaximo = cv2.getTrackbarPos('S maximo', 'configuracion')
    Vminimo = cv2.getTrackbarPos('V minimo', 'configuracion')
    Vmaximo = cv2.getTrackbarPos('V maximo', 'configuracion')

    Hmin = cv2.getTrackbarPos('H minimo', 'configuracion imagen')
    Hmax = cv2.getTrackbarPos('H maximo', 'configuracion imagen')
    Smin = cv2.getTrackbarPos('S minimo', 'configuracion imagen')
    Smax = cv2.getTrackbarPos('S maximo', 'configuracion imagen')
    Vmin = cv2.getTrackbarPos('V minimo', 'configuracion imagen')
    Vmax = cv2.getTrackbarPos('V maximo', 'configuracion imagen')
 
    # Aqui mostramos la imagen en blanco o negro segun el rango de colores.
    
    bn_img = cv2.inRange(hsv, np.array((Hminimo,Sminimo,Vminimo)), np.array((Hmaximo,Vmaximo,Smaximo)))
    vn_img = cv2.inRange(hsb, np.array((Hmin,Smin,Vmin)), np.array((Hmax,Vmax,Smax)))
 
    # Limpiamos la imagen de imperfecciones con los filtros erode y dilate
    
    bn_img = cv2.erode (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations = 1)
    bn_img = cv2.dilate (bn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),iterations = 1)
    
    vn_img = cv2.erode (vn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)),iterations = 1)
    vn_img = cv2.dilate (vn_img,cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)),iterations = 1)
    
    # Localizamos la posicion del centro del objeto
    
    M = cv2.moments(bn_img)
    if M['m00']>50000:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    # Mostramos un circulo verde en la posicion en la que se encuentra el centro del objeto
        
        cv2.circle (frame,(cx,cy),20,(0,255,0), 2)
 
    S = cv2.moments(vn_img)
    if S['m00']>50000:
        cx1 = int(S['m10']/S['m00'])
        cy1 = int(S['m01']/S['m00'])
            
        cv2.circle (frame,(cx1,cy1),20,(255,0,0), 2)
 
    # Creamos las ventanas de salida y configuracion
    
    cv2.imshow('Salida', frame)
    cv2.imshow('inRange', bn_img)
    cv2.imshow('Range', vn_img)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Indicamos que al pulsar "q" el programa se cierre
        break

cap.release()
cv2.destroyAllWindows()
