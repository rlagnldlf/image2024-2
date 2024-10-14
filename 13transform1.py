import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]

print(img.shape)
print(f'={rows}')

dx, dy = 100, 50

mtrx = np.float32([[2,0,dx], [0,2,dy]])
dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()