import cv2
#import numpy as np

imagen= cv2.imread('foto.png')
cv2.imshow('Prueba de imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows