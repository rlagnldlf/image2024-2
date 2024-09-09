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

# 2024-9 원그리기
# 다각형 그리기
img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.circle(img, (150, 150), 100, (255,0,0))
cv2.circle(img, (300, 150), 70, (0,255, 0), 5)
cv2.circle(img, (400, 150), 50, (0,0,0), -1)

cv2.ellipse(img, (50, 300), (50, 50), 0,0,360, (0,0,255))
cv2.ellipse(img, (150, 300), (50,50), 0, 0, 180, (255, 0, 0))
cv2.ellipse(img, (200, 300), (50,50), 0, 181, 360, (0, 0, 255))

# 납작한 타원
cv2.ellipse(img, (325, 300), (75, 50), 0, 0, 360, (0, 255, 0))
# 길쭉한 타원
cv2.ellipse(img, (450, 300), (50, 75), 0, 0, 360, (255, 0, 255))

# 원점 (50, 425), (50, 75), 회전 15
cv2.ellipse(img, (50, 425), (50, 75), 15, 0, 360, (0, 255, 0))
# 원점 (200, 425), (50, 75), 회전 45
cv2.ellipse(img, (200, 425), (50, 75), 45, 0, 360, (0, 255, 0))

# (350, 425)  홀쭉한 타원 45도 회전, 아랫반원
cv2.ellipse(img, (350, 425), (50, 75), 45, 0, 180, (0, 0, 255))
# (400, 425)  홀쭉한 타원 45도 회전, 윗반원
cv2.ellipse(img, (400, 425), (50, 75), 45, 180, 360, (0, 0, 255))

cv2.imshow('polygon', img)
cv2.waitKey(0)
cv2.destroyAllWindows()