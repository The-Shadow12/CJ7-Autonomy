import cv2
from pyzbar.pyzbar import decode

def decodificar_qr(frame_gris, frame_color):
    _, frame_blanco_negro = cv2.threshold(frame_gris, 100, 255, cv2.THRESH_BINARY)

    codigos_detectados = decode(frame_blanco_negro)
    texto_qr = None
    
    frame_debug = frame_color.copy()

    for codigo in codigos_detectados:

        texto_qr = codigo.data.decode('utf-8')
        
        puntos = codigo.polygon
        if len(puntos) == 4:
            pts = [tuple(puntos[i]) for i in range(4)]
            cv2.line(frame_debug, pts[0], pts[1], (0, 255, 0), 3)
            cv2.line(frame_debug, pts[1], pts[2], (0, 255, 0), 3)
            cv2.line(frame_debug, pts[2], pts[3], (0, 255, 0), 3)
            cv2.line(frame_debug, pts[3], pts[0], (0, 255, 0), 3)
            
            
            cv2.putText(frame_debug, texto_qr, (pts[0][0], pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
    return texto_qr, frame_debug