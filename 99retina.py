import cv2
from retinaface import RetinaFace
import time
start = time.time()
img_path = './img/graduate.jpg'
faces = RetinaFace.detect_faces(img_path)
img = cv2.imread(img_path)
face = faces['face_1']
for j in range(len(faces)):
    i = 1
    i += j
    face = faces[f'face_{i}']
    cv2.rectangle(img,(faces[f'face_{i}']['facial_area'][0],faces[f'face_{i}']['facial_area'][1]),(faces[f'face_{i}']['facial_area'][2],faces[f'face_{i}']['facial_area'][3]),(0,255,0),2)
    cv2.putText(img, f"{face['score']:.3f}", (faces[f'face_{i}']['facial_area'][0],faces[f'face_{i}']['facial_area'][1]), cv2.FONT_HERSHEY_PLAIN,
                1, (0, 255, 0))
# cv2.rectangle(img,(faces['face_1']['facial_area'][0],faces['face_1']['facial_area'][1]),(faces['face_1']['facial_area'][2],faces['face_1']['facial_area'][3]),(0,255,0),2)

cv2.imshow('face', img)
end = time.time()
print((end-start) * 1000)
cv2.waitKey(0)
cv2.destroyAllWindows()