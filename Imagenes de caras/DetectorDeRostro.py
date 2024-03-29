import cv2
#import numpy as np

imagen= cv2.imread('messi.png')
if imagen is None:
    print('Error: No se pudo cargar la imagen.')
else:
    cv2.imshow('Prueba de imagen', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()