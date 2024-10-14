import cv2
import matplotlib.pylab as plt

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0],None,  [256], [0, 255])

img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
hist_norm = cv2.calcHist(img_norm, [0], None, [256], [0, 255])

img_eq = cv2.equalizeHist(img)
hist_eq = cv2.calcHist([img_eq],[0],  None, [256], [0, 255] )

cv2.imshow('img', img)
cv2.imshow('img_norm', img_norm)
cv2.imshow('img_eq', img_eq)

plt.subplot(1, 3, 1)
plt.plot(hist)
plt.subplot(1, 3, 2)
plt.plot(hist_norm)
plt.subplot(1, 3, 3)
plt.plot(hist_eq)
plt.show()