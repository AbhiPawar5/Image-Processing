import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "C:\\Users\\Viraj Pawar\\Desktop\\WCE SEM 1\\Image Processing"

org_img = cv2.imread(path + "\\myImage.jpg",0)
median_input = cv2.imread(path + "\\myImageBad2.jpg",0)

mask = np.ones((5,5),np.float32)/25

average_image = cv2.filter2D(org_img,-1,mask)
gaussian_image = cv2.GaussianBlur(org_img,(5,5),0)
median_blur = cv2.medianBlur(median_input,5)


cv2.imshow("Gaussian Blur",gaussian_image)
cv2.imshow("Weighted Average",average_image)
cv2.imshow("Median Image",median_blur)
cv2.imshow("Median Original Image",median_input)
cv2.imshow("Original Image",org_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
