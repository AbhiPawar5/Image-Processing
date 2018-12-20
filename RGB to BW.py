#OpenCV import statement
import cv2

#Absolute path of image to be read. 0 is passed to read it directly as Grayscale image
gray_img = cv2.imread("C:\\Users\\Abhishek Pawar\\Desktop\\myImage.jpg",0)

#function to show images
cv2.imshow("Grayscale Image",gray_img)

#this variable is calculated with logic 255/2=127 to divide pixels as B or W
threshold_value = 127

#Calculate and process image with threshold value as 127 in threshold_value variable
manual_threshold_img = cv2.threshold(gray_img,threshold_value,255,cv2.THRESH_BINARY)[1]

#We use OTSU method to get optimal threshold value for any image,unlike manual setting
opt_value = cv2.threshold(gray_img,0,255,cv2.THRESH_OTSU)[0]
otsu_threshold_img = cv2.threshold(gray_img,0,255,cv2.THRESH_OTSU)[1]

#returns optimal value calculated using OTSU's algorithm
print("Optimal Threshold Value found by Otsu : ",opt_value)
cv2.imshow("Manual Thresholding Image",manual_threshold_img)
cv2.imshow("OTSU Thresholding Image",otsu_threshold_img)

#wait for user to press any key and destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()