import cv2
import numpy as np
from matplotlib import pyplot as plt

org_img = cv2.imread("C:\\Users\\Abhishek Pawar\\Desktop\\Image Processing\\myImage.jpg",0)

f = np.fft.fft2(org_img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(org_img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()