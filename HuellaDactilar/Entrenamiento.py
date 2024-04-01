## Se usa LBPH para entrenar el modelo
# Se reutiliza el codigo para el entrenamiento de reconocimiento facial
import cv2
import os
import numpy as np

dataPath = 'HuellaDactilar/Data' 
huellas= os.listdir(dataPath)
modelo_path = 'HuellaDactilar/modeloBPH.xml'

print('Lista de huellas: ', huellas)

labels =[]
fingerprintsData=[]
label=0

for nameDir in huellas:
    personPath= dataPath+ '/' +nameDir
    print('Leyendo las imágenes')

    for fileName in os.listdir(personPath):
        print('Huellas', nameDir+ '/' + fileName)
        labels.append(label)
        fingerprintsData.append(cv2.imread(personPath+'/'+fileName,0))
    label = label+1

fingerprint_recognizer = cv2.face.LBPHFaceRecognizer_create()

print('Entrenando')

fingerprint_recognizer.train(fingerprintsData, np.array(labels))

print('Ruta del modelo:', modelo_path)
try:
    fingerprint_recognizer.write(modelo_path)
    print('Modelo almacenado exitosamente')
except Exception as e:
    print('Error al guardar el modelo:', e)
