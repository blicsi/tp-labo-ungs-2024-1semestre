import cv2
import numpy as np
import os

dataPath = 'HuellaDactilar/Data' 
huellas= os.listdir(dataPath)
modelo_path = 'HuellaDactilar/modeloFinger.xml'

sift = cv2.SIFT_create()
svm = cv2.ml.SVM_create()

descriptores = []
etiquetas = []

# Leer y procesar las imágenes de HuellaDactilar/Data
for huella in huellas:
    fingerStored = cv2.imread(os.path.join(dataPath, huella), cv2.IMREAD_GRAYSCALE)
    
    # Añadir descriptores y etiquetas
    keypoints, descriptor = sift.detectAndCompute(fingerStored, None)
    if descriptor is not None:
        descriptores.append(descriptor)
        etiquetas.append(1)  # Etiqueta 1 para huellas del usuario correcto

# Convierte en arrays numpy
descriptores_np = np.vstack(descriptores)
etiquetas_np = np.array(etiquetas)

# Entrenar el clasificador
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))

print('Entrenando...')
svm.train(descriptores_np, cv2.ml.ROW_SAMPLE, etiquetas_np)

print('Ruta del modelo:', modelo_path)
try:
    svm.write(modelo_path)
    print('Modelo almacenado exitosamente')
except Exception as e:
    print('Error al guardar el modelo:', e)