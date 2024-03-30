import cv2
import os
import numpy as np

dataPath = 'ReconocimientoFacial/Data' 
listaPersonas= os.listdir(dataPath)

print('Lista de personas: ', listaPersonas)

labels =[]
facesData=[]
label=0

for nameDir in listaPersonas:
    personPath= dataPath+ '/' +nameDir
    print('Leyendo las imagenes')

    for fileName in os.listdir(personPath):
        print('Rostros', nameDir+ '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath+'/'+fileName,0)
    label = label+1

face_recognizer = cv2.face.EigenFaceRecognizer_create()

print('Entrenando')

face_recognizer.train(facesData, np.array(labels))

face_recognizer.write('modeloEigenFace.xml')

print('Modelo almacenado')
