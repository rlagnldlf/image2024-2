import cv2
import numpy as np
# img = np.full((500,500,3), 255, dtype=np.uint8)

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

cv2.rectangle(img, (50,50), (150,150), (255,0,0), 10)
cv2.rectangle(img, (300,300), (100,100), (0,255,0), 10)
cv2.rectangle(img, (450,200), (200,450), (0,0,255), -1)
cv2.imshow('polygon', img)
cv2.waitKey(0)
cv2.destroyAllWindows()