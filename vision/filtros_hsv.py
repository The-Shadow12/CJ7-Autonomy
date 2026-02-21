import cv2
import numpy as np

def detectar_rojo(frame_color):

    hsv = cv2.cvtColor(frame_color, cv2.COLOR_BGR2HSV)
    
    rango_bajo_1 = np.array([0, 120, 70])
    rango_alto_1 = np.array([10, 255, 255])
    rango_bajo_2 = np.array([170, 120, 70])
    rango_alto_2 = np.array([180, 255, 255])
    
    
    mascara1 = cv2.inRange(hsv, rango_bajo_1, rango_alto_1)
    mascara2 = cv2.inRange(hsv, rango_bajo_2, rango_alto_2)
    mascara_roja = mascara1 + mascara2 
    
    
    kernel = np.ones((5,5), np.uint8)
    mascara_roja = cv2.morphologyEx(mascara_roja, cv2.MORPH_OPEN, kernel)
    
    
    contornos, _ = cv2.findContours(mascara_roja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    frame_debug = frame_color.copy()
    centro_x, centro_y = None, None
    
    if contornos:
       
        contorno_maximo = max(contornos, key=cv2.contourArea)
        area = cv2.contourArea(contorno_maximo)
        
       
        if area > 500:
            M = cv2.moments(contorno_maximo)
            if M["m00"] != 0:
                centro_x = int(M["m10"] / M["m00"])
                centro_y = int(M["m01"] / M["m00"])
                
                
                x, y, w, h = cv2.boundingRect(contorno_maximo)
                cv2.rectangle(frame_debug, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.circle(frame_debug, (centro_x, centro_y), 5, (255, 0, 0), -1)
                cv2.putText(frame_debug, f"X:{centro_x} Y:{centro_y}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
    return mascara_roja, frame_debug, centro_x, centro_y