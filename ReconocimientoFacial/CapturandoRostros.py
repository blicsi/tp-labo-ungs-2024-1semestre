import cv2
import os
import imutils

persona= 'Patricio'
dataPath = 'ReconocimientoFacial/Data'
personaPath = dataPath + '/' + persona


if not os.path.exists(personaPath):
    print('Carpeta creada: ', personaPath)
    os.makedirs(personaPath)

