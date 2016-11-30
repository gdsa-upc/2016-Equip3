import numpy as np
import cv2

from matplotlib import pyplot as plt

img = cv2.imread('E:/universidad/GDSA/masia_freixa/masia_freixa/Masia_Freixa_00.jpg',0)
# el 0 ho passa a nivells de gris

# Iniciem el detector ORB
orb = cv2.ORB()

# Detecta els punts clau a la imatge
kp = orb.detect(img,None)

# processa els descriptors amb l'ORB
kp, des = orb.compute(img, kp)

# dibuixa els descriptors sobre la imatge amb representació segons la importància
img2 = cv2.drawKeypoints(img,kp,flags=4)

plt.imshow(img2),plt.show()