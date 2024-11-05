import cv2
import numpy as np
from sklearn.metrics import accuracy_score

# 'image.jpg'
img = cv2.imread('data/tutori/tutorial/single_pic/PIC/XXX.tif')


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_liquid = np.array([0, 50, 50])
upper_liquid = np.array([10, 255, 255])

lower_gas = np.array([110, 50, 50])
upper_gas = np.array([130, 255, 255])


mask_liquid = cv2.inRange(hsv, lower_liquid, upper_liquid)
mask_gas = cv2.inRange(hsv, lower_gas, upper_gas)


mask_liquid = mask_liquid.reshape(-1)
mask_gas = mask_gas.reshape(-1)
labels = labels.reshape(-1)

predictions = np.zeros_like(labels)
predictions[mask_liquid == 255] = 1
predictions[mask_gas == 255] = 0

accuracy = accuracy_score(labels, predictions)
print('Accuracy:', accuracy)
