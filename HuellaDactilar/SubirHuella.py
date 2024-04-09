import cv2
import os

def subir_huella(path):
    dataPath = 'HuellaDactilar/Data'
    try:
        image = cv2.imread(path)
        filename = os.path.basename(path)
        
        # Ruta de guardado
        save_path = os.path.join(dataPath, filename)
        
        cv2.imwrite(save_path, image)
        return True
    except Exception as e:
        print("Error al guardar la imagen:", str(e))
        return False
