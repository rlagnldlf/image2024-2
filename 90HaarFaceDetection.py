import cv2
import numpy as np
from cv2.data import haarcascades
from PIL import Image, ImageFont, ImageDraw
import time
start = time.time()

# 얼굴과 눈을 감지하기 위한 CascadeClassifier 로드
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('./img/graduate.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 감지
faces = face_cascade.detectMultiScale(gray)
for i in range(len(faces)):
    x, y, w, h = faces[i]

    # 얼굴 중앙 좌표 및 타원 축 계산
    center = (x + w // 2, y + h // 2)
    axes = (w // 2, h // 2)  # 가로와 세로 축 반
    angle = 0  # 타원의 회전 각도 (얼굴에 맞추려면 조정 가능)

    # 얼굴에 타원 그리기
    cv2.ellipse(img, center, axes, angle, 0, 360, (255, 0, 0), 2)

    # 눈 감지 및 눈에 사각형 그리기
    eyes = eye_cascade.detectMultiScale(gray[y:y + h, x:x + w])
    for j in range(len(eyes)):
        x1, y1, w1, h1 = eyes[j]
        cv2.rectangle(img, (x + x1, y + y1), (x + x1 + w1, y + y1 + h1), (0, 255, 0), 2)

# OpenCV 이미지를 PIL 이미지로 변환
img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))




# 결과 이미지 보여주기
cv2.imshow('Image', img)
end = time.time()
print((end-start) * 1000)
cv2.waitKey(0)
cv2.destroyAllWindows()