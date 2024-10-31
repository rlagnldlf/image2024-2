import copy

import cv2
from matplotlib.pyplot import imread

rate = 10
img = imread('./img/taekwonv1.jpg')
img2 = copy.deepcopy(img)
x, y, w, h = cv2.selectROI('mosaic', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    roi = cv2.resize(roi, (w//rate, h//rate))
    roi = cv2.resize(roi, (w, h))
    img2[y:y+h, x:x+w] = roi
    cv2.imshow('mosaic', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()