##OpenCV import statement
import cv2

#Absolute path of image to be read.150x150 size
img = cv2.imread("C:\\Users\\win-7\\Desktop\\interpolate_input.jpg")

#variables holding various interpolation processed images
linear_interpolation = cv2.resize(img,(600,600),interpolation=cv2.INTER_LINEAR)
nearest_interpolation = cv2.resize(img,(600,600),interpolation=cv2.INTER_NEAREST)
cubic_interpolation = cv2.resize(img,(600,600),interpolation=cv2.INTER_CUBIC)
org_interpolation = cv2.resize(img,(600,600))

#Shows processed and input images to screen
cv2.imshow("Original Input Image",img)
cv2.imshow("Original Interpolated Image",org_interpolation)
cv2.imshow("Cubic Interpolation",cubic_interpolation)
cv2.imshow("Linear Interpolation",linear_interpolation)
cv2.imshow("Nearest Interpolation",nearest_interpolation)

#wait for user to press any key and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()