import cv2
import os

def reconocimiento_huella(path):
    dataPath = 'HuellaDactilar/Data' 
    
    fingerGray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    sift = cv2.SIFT_create()
    FBM = cv2.FlannBasedMatcher(dict(algorithm=1, tress=5), dict(checks=2))
        
    # Extraer descriptores de la huella y validarlos
    keypoints, descriptors = sift.detectAndCompute(fingerGray, None)
    if descriptors is None:
        print("No se pudieron calcular los descriptores de la huella del usuario.")
        return False

    for huella in os.listdir(dataPath):
        huellaInPath = cv2.imread(os.path.join(dataPath, huella))
        
        keypointsInPath, descriptorsInPath = sift.detectAndCompute(huellaInPath, None)
        if descriptorsInPath is None:
            print("No se pudieron calcular los descriptores de la huella almacenada: " + os.path.join(dataPath, huella))
            continue
        
        matches = FBM.knnMatch(descriptors, descriptorsInPath, k=2)
        
        matchesArr = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                matchesArr.append(m)
        
        if len(matchesArr) > 95:
            print("Coincidencia encontrada")
            return True
        
    print("Las huellas no coinciden")
    return False