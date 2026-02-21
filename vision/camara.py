import cv2

class CamaraDron:
    def __init__(self, indice_camara=0):

        print("[VISIÓN] Iniciando cámara...")
        self.cap = cv2.VideoCapture(indice_camara)
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            raise Exception("¡ERROR! No se pudo abrir la cámara.")
        print("[VISIÓN] Cámara lista y operativa.")

    def leer_frame(self):
        exito, frame = self.cap.read()
        if not exito:
            return False, None, None


        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        return True, frame, frame_gris

    def apagar(self):

        self.cap.release()
        cv2.destroyAllWindows()
        print("[VISIÓN] Cámara apagada.")

#'''
if __name__ == "__main__":
    from filtros_hsv import detectar_rojo
    
    camara = CamaraDron(indice_camara=2)
    
    try:
        while True:
            exito, frame_color, frame_gris = camara.leer_frame()
            
            if exito:
                
                mascara, frame_con_dibujo, cx, cy = detectar_rojo(frame_color)
                
                
                cv2.imshow("Vision Maquina (Mascara)", mascara)
                cv2.imshow("Vision Humana (Centroide)", frame_con_dibujo)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nPrueba interrumpida por el usuario.")
    finally:
        camara.apagar()
#'''
        
'''
if __name__ == "__main__":

    from detector_qr import decodificar_qr
    
    camara1 = CamaraDron(indice_camara=0)
    camara2 = CamaraDron(indice_camara=2)
    
    try:
        while True:
            exito, frame_color, frame_gris = camara1.leer_frame()
            exito2, frame_color2, frame_gris2 = camara2.leer_frame()
            
            if exito and exito2:
                texto_encontrado, frame_con_dibujo = decodificar_qr(frame_gris, frame_color)
                texto_encontrado2, frame_con_dibujo2 = decodificar_qr(frame_gris2, frame_color2)

                if texto_encontrado and texto_encontrado2:
                    print(f"[ALERTA] QR Detectado: {texto_encontrado}")
                    print(f"[ALERTA2] QR Detectado: {texto_encontrado2}")
                
                cv2.imshow("Vista Dron CJ7 (Lector QR)", frame_con_dibujo)
                cv2.imshow("Vista Dron2 CJ7 (Lector QR)", frame_con_dibujo2)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nPrueba interrumpida por el usuario.")
    finally:
        camara1.apagar()
        camara2.apagar()
'''