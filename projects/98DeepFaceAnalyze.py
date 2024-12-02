import cv2
from deepface import DeepFace
from sympy.physics.units import action

img_file = './img/children.jpg'
image = cv2.imread(img_file)

actions = ['age', 'gender', 'race', 'emotion']
ar = DeepFace.analyze(img_file, actions=actions)
print(ar)
cv2.rectangle(image, (144, 94), (144 + 122, 94 + 122), (255, 0, 0), 2)
cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()