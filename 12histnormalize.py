import cv2
import matplotlib.pylab as plt

img = cv2.imread('./img/abnormal.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist)
plt.show()

img_norm = (img - img.min()) * 255 / (img.max() - img.min())
img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('', img)
cv2.imshow('imgnorm', img_norm)
cv2.imshow('imgnorm_cv', img_normcv)
cv2.waitKey(0)
cv2.destroyAllWindows()