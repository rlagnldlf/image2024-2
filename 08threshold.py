import cv2
import numpy as np
import matplotlib.pylab as plt

# 첫번째 방법
# 127로 중간숫자를 고정
img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)
thresh_np[img > 171] = 255
thresh_np[(128<img) & (img<171)] = 128
thresh_np[(64 < img) & (img < 128)] = 64
#두번째 방법
thresh_np = np.zeros_like(img)
thresh_np[img > 64] = 64
thresh_np[img > 128] = 128
thresh_np[img > 171] = 255
print('img', img)
# 세번째 방법
thresh_np = np.zeros_like(img)
ysize, xsize = img.shape
for x in range(xsize):
    for y in range(ysize):
        if(img[y,x] > 64):
            thresh_np[y,x] = 64
        if (img[y, x] > 128):
            thresh_np[y, x] = 128
        if(img[y,x] > 171):
            thresh_np[y,x] = 255

_, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('thr', thresh_np)
cv2.imshow('IMG', img)
cv2.imshow('cv2', thresh_cv)
cv2.waitKey()
cv2.destroyAllWindows()

# 두번째방법
# 이미지에 따라 문턱값을 이리저리 조정 80, 100, 120, 140
img = cv2.imread('./img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
_, t80 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, t100 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, t120 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, t140 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)

cv2.imshow('t80', t80)
cv2.imshow('t100', t100)
cv2.imshow('t120', t120)
cv2.imshow('t140', t140)
cv2.waitKey()
cv2.destroyAllWindows()

# 세번째 방법
# 0tsu 알고리즘 적용
_, t130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
t, totsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(t)
cv2.imshow('t130', t130)
cv2.imshow('totus', totsu)
cv2.waitKey()
cv2.destroyAllWindows()

# 네번째 방법
# 적응형 문턱값 적용 : 주위값에 따라 달라짐, blk_size = 9
img = cv2.imread('./img/sudoku.png', cv2.IMREAD_GRAYSCALE)
blk_size = 9
C = 5

ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(ret)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

cv2.imshow('img', img)
cv2.imshow('totus', th1)
cv2.imshow('tmean', th2)
cv2.imshow('tgaussian', th3)

cv2.waitKey()
cv2.destroyAllWindows()
