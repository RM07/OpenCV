import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rohan Meena.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img,cmap="gray",interpolation="bicubic")
#plt.plot([500,2000],[800,100],"c",linewidth = 5)
#plt.show()

cv2.imwrite("watchgray.png",img)