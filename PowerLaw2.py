import cv2
import numpy as np


path = "C:\\Users\\Viraj Pawar\\Desktop\\WCE SEM 1\\Image Processing\\"

image = cv2.imread(path + "hist_image.jpg")

new_image = np.zeros(image.shape,image.dtype)

power = 1.08
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(image[y,x,c] ** power, 0, 255)
            
cv2.imshow('Original Image', image)
cv2.imshow('New Image', new_image)
# Wait until user press some key
cv2.waitKey(0) 
cv2.destroyAllWindows()