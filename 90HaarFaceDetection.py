import cv2
import numpy as np
from cv2.data import haarcascades
from PIL import Image, ImageFont, ImageDraw

# 얼굴과 눈을 감지하기 위한 CascadeClassifier 로드
face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('./img/children.jpg')
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

# 텍스트를 그릴 수 있도록 준비
draw = ImageDraw.Draw(img_pil)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 사용할 폰트 경로
font = ImageFont.truetype(font_path, 36)  # 폰트 크기 설정

# 텍스트 추가
text = "김휘일 중간과제"

# 텍스트의 경계 상자 계산
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# 텍스트 위치 (이미지 하단 중앙)
text_x = img.shape[1] - text_w - 20
text_y = img.shape[0] - text_h - 20  # 이미지 하단에서 약간 위쪽으로

draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))  # 검정 텍스트

# PIL 이미지를 다시 OpenCV 이미지로 변환
img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# 결과 이미지 보여주기
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
