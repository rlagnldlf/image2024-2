import cv2
import numpy as np
from cv2.data import haarcascades

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')
img = cv2.imread('./img/graduate.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
for i in range(len(faces)):
    x, y, w, h = faces[i]
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    eyes = eye_cascade.detectMultiScale(gray[y:y+h, x:x+w])
    for j in range(len(eyes)):
        x1, y1, w1, h1 = eyes[j]
        cv2.rectangle(img, (x+x1,y+y1), (x+x1+w1, y+y1+h1), (0, 255, 0), 2)

cv2.imshow('gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()