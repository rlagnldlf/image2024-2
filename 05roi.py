import cv2
import numpy as np
img = cv2.imread('./img/sunset.jpg')

cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows()