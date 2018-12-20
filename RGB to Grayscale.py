#OpenCV import statement
import cv2,numpy as np

#Absolute path of image to be read. 0 is passed to read it directly as Grayscale image
path = "C:\\Users\\Abhishek Pawar\\Desktop\\"
grayimg = cv2.imread(path + "myImage.jpg",cv2.IMREAD_GRAYSCALE)

#function to show images
cv2.imshow("Grayscale Image",grayimg)

#wait for user to press any key and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
