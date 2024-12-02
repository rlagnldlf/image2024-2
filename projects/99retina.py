from retinaface import RetinaFace
import cv2

imgfile = './img/children.jpg'
resp = RetinaFace.detect_faces(imgfile)
print(resp)
image = cv2.imread(imgfile)
face1 = resp['face_1']
farea = face1['facial_area']
print(farea)
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255, 0), 2)
face1 = resp['face_2']
farea = face1['facial_area']
print(farea)

# cv2.rectangle(image, (400, 95), (490, 207), (0, 255, 0), 2)
cv2.rectangle(image, (farea[0], farea[1]), (farea[2], farea[3]), (0, 255, 0), 2)

cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
