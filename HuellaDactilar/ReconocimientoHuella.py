import cv2
import os

dataPath = 'HuellaDactilar/Data' 
modelo_path = 'HuellaDactilar/modeloFinger.xml'
userFinger = 'HuellaDactilar/userFinger.jpg'
userFingerWrong = 'HuellaDactilar/userFingerWrong.jpg'

# Reemplazar userFinger por userFingerWrong
fingerGray = cv2.imread(userFinger, cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()
    
# Extraer descriptores de la huella y validarlos
keypoints, descriptors = sift.detectAndCompute(fingerGray, None)
if descriptors is None:
    print("No se pudieron calcular los descriptores de la huella del usuario.")

# Lee el modelo y compara
sift.read(modelo_path)
matches = sift.knnMatch(descriptors, k=2)

matchesArr = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        matchesArr.append(m)

# Umbral de coincidencias
if len(matchesArr) > 95:
    print("Coincidencia encontrada")

print("Las huellas no coinciden")