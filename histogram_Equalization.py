import cv2
from matplotlib import pyplot as plt

path = "C:\\Users\\Viraj Pawar\\Desktop\\WCE SEM 1\\Image Processing\\"

original_image = cv2.imread(path + "hist_image.jpg",0)
cv2.imshow("Original Input Image",original_image)

equalized_image = cv2.equalizeHist(original_image)
cv2.imshow("Equalized Image",equalized_image)

hist_equalized = cv2.calcHist([equalized_image],[0],None,[256],[0,256])  
hist_original = cv2.calcHist([original_image],[0],None,[256],[0,256])

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(1)
plt.title("Equalized Image")
plt.plot(hist_equalized)

plt.figure(2)
plt.title("Original Image")
plt.plot(hist_original)
plt.show()