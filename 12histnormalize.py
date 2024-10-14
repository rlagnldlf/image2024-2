import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist)
plt.show()

# 분자의 오버플로우에의한 에러
# img_norm = ((img - img.min()) * 255) / (img.max() - img.min())

# 첫번째 방법
# 나누어 주고 나중에 255를 곱함
# img_norm = ((img - img.min()) / (img.max() - img.min())) * 255


# 두번째 방법
# 형변환을 유도
# img_norm = ((img - img.min()) * 255.0) / (img.max() - img.min())

# 세번째 방법
# 직접 형변환
img_f = img.astype(np.float32)
img_norm = (img_f - img_f.min()) * 255 / (img_f.max() - img_f.min())

img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])
hist_normcv = cv2.calcHist([img_normcv], [0], None, [256], [0, 255])

plt.subplot(1, 3, 1)
plt.plot(hist)
plt.subplot(1, 3, 2)
plt.plot(hist_norm)
plt.subplot(1, 3, 3)
plt.plot(hist_normcv)
plt.show()

plt.plot(hist_norm)
plt.show()
plt.plot(hist_normcv)
plt.show()

print(img_norm)
cv2.imshow('', img)
cv2.imshow('imgnorm', img_norm.astype(np.uint8))
cv2.imshow('imgnorm_cv', img_normcv)
cv2.waitKey(0)
cv2.destroyAllWindows()