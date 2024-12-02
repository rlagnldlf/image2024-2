import cv2
from deepface import DeepFace
import time
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
img_file = './img/graduate.jpg'
image = cv2.imread(img_file)
# backends = ['fastmtcnn', 'mediapipe', 'yolov8']
backends = [ 'dlib', 'opencv', 'ssd', 'mtcnn', 'retinaface', 'yunet', 'centerface']
DeepFace_time = []
for i in backends:
    start = time.time()
    detections = DeepFace.extract_faces(img_path=img_file,
                                        detector_backend=i,
                                        enforce_detection=False)
    print(detections)
    end = time.time()
    DeepFace_time.append(round((end - start) * 1000, 2))

print(DeepFace_time)
print(backends)

plt.figure(figsize=(10, 6))
plt.bar(backends, DeepFace_time, color='skyblue')
plt.xlabel('Backends')
plt.ylabel('Time (ms)')
plt.title('Processing Time for Each Backend')

# 그래프에 값 표시
for i in range(len(DeepFace_time)):
    plt.text(i, DeepFace_time[i] + 100, f'{DeepFace_time[i]:.2f}', ha='center')

plt.show()

