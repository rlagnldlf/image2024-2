import cv2
import numpy as np

img = cv2.imread('./img/sudoku.png')

# 컬러 이미지는 흑백변환
# img = cv2.imread('./img/children.jpg', cv2.IMREAD_GRAYSCALE)

gx_kernel = np.array([[-1, 1]])
gy_kernel = np.array([[-1], [1]])

edge_gx = cv2.filter2D(img, -1, gx_kernel)
edge_gy = cv2.filter2D(img, -1, gy_kernel)

cv2.imshow('sudoku', img)
cv2.imshow('edge x', edge_gx)
cv2.imshow('edge y', edge_gy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# sobel 커널 만들기
gx_k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy_k = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
edge_gxs = cv2.filter2D(img, -1, gx_k)
edge_gys = cv2.filter2D(img, -1, gy_k)

sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(img, -1, 0, 1, ksize=3)
sobelxy = cv2.Sobel(img, -1, 1, 1, ksize=3)

cv2.imshow('sudoku', img)
cv2.imshow('sedge x', edge_gxs)
cv2.imshow('sedge y', edge_gys)

cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('sobelxy', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Scharr 필터
gx_ksc = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
gy_ksc = np.array([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])
scharx = cv2.filter2D(img, -1, gx_ksc)
schary = cv2.filter2D(img, -1, gy_ksc)

# Laplactian 필터
gx_kl = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
lapl = cv2.filter2D(img, -1, gx_kl)
laplf = cv2.Laplacian(img, -1)
# Canny 필터
canny = cv2.Canny(img, 50, 150)

cv2.imshow('scharx', scharx)
cv2.imshow('schary', schary)
cv2.imshow('laplace', lapl)
cv2.imshow('laplacian', laplf)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()