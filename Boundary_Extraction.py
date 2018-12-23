#OpenCV import statement
import cv2,numpy as np

#Absolute path of image to be read. 0 is passed to read it directly as Grayscale image
img = cv2.imread("C:\\Users\\Abhishek Pawar\\Desktop\\sample.jpg")

kernel = np.ones((5,5),np.int8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#function to show images
cv2.imshow("Detected Image",gradient)
cv2.imshow("Original Image",img)

#wait for user to press any key and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()