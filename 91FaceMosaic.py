# 2024.10.31
# Haar filter를 사용하여
import cv2

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')
img = cv2.imread('./img/smilings.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
rate = 10
for face in faces:
    fx, fy, fw, fh = face
    roi = img[fy:fy+fh, fx:fx+fw]
    roi = cv2.resize(roi, (fw//rate, fh//rate ))
    roi = cv2.resize(roi, (fw, fh))
    img[fy:fy+fh, fx:fx+fw] = roi

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()