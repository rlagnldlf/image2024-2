import cv2
import numpy as np

img = cv2.imread('./img/girl.jpg')

kernel = np.ones((5,5))/25
print(kernel)

blured = cv2.filter2D(img, -1, kernel)
cv2.imshow('org', img)
cv2.imshow('blur', blured)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('./img/gaussian_noise.jpg')
kernel = np.ones((5,5))/25
blured = cv2.filter2D(img, -1, kernel)

k1 = np.array([[1,2,1],
               [2,4,2],
               [1,2,1]])/16

k2 = cv2.getGaussianKernel(5, 0)

print(k2)

k1img = cv2.filter2D(img, -1, k1)
k2img = cv2.filter2D(img, -1, k2 * k2.T)
k3img = cv2.medianBlur(img, 5)
k4img = cv2.bilateralFilter(img, 5, 75, 75)

cv2.imshow('noise', img)
cv2.imshow('blur', blured)
cv2.imshow('k1', k1img)
cv2.imshow('k2', k2img)
cv2.imshow('median', k3img)
cv2.imshow('bilateral', k4img)

cv2.waitKey(0)
cv2.destroyAllWindows()