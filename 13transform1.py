import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols = img.shape[0:2]

print(img.shape)
print(f'={rows}')

dx, dy = 100, 50

mtrx = np.float32([[1,0,dx],
                   [0,1,dy]])
dst1 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))
dst2 = cv2.warpAffine(img, mtrx, (cols+dx,rows+dy),
                     None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))
dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows + dy),
                      None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width, _ = img.shape
# height, width = img.shape[0:2] 와 같음

m_small = np.float32([[0.5, 0, 0],
                      [0, 0.5, 0]])
m_big = np.float32([[1.5, 0, 0],
                    [0, 1.5, 0]])
dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
dst2 = cv2.warpAffine(img, m_big, (int(height*1.5), int(width*1.5)))
dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)),
                      None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, m_small, (int(height*1.5), int(width*1.5)),
                      None, cv2.INTER_CUBIC)
cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()
