import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('C:\\Users\\guest123\\Pictures\\standard_test_images\\2.png')
img1= 255 - img


cv2.imshow('RESULT',img1)
cv2.imshow('ORIGNAL IMAGE',img)
cv2.waitKey(100000)
cv2.destroyAllWindows()
