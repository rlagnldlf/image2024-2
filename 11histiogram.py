import cv2
import matplotlib.pylab as plt

img = cv2.imread('./img/mountain.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(hist)
plt.show()
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('./img/smilings.jpg')
cv2.imshow('img', img)

channels = cv2.split(img)
colors = ('b', 'g', 'r')
for(ch, color) in zip(channels, colors):
    print(ch)
    print(color)
    hist = cv2.calcHist([ch], [0], None, [256], [0, 255])
    plt.plot(hist, color = color)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()