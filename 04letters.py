import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


img = np.full((500, 500, 3), 255, dtype=np.uint8)

#sans-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
#sans-serif normal
cv2.putText(img, "Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
#sans-serif bold
cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
#sans-serif normal
cv2.putText(img, "Simplex X 2", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250))

#serif small
cv2.putText(img, "Complex small", (50,180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
#serif small
cv2.putText(img, "Complex", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
#serif bold
cv2.putText(img, "Complex", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
#serif normalx2
cv2.putText(img, "Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

cv2.putText(img, "Complex", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))

font_path = "C:/Windows/Fonts/malgun.ttf"  # 폰트 경로 (Windows 기준)
font = ImageFont.truetype(font_path, 40)  # 폰트 크기 설정
# 3. OpenCV 이미지를 Pillow 이미지로 변환
img_pil = Image.fromarray(img)

# 4. Pillow의 ImageDraw 객체 생성
draw = ImageDraw.Draw(img_pil)

# 5. 한글 텍스트 추가 ("아름다운강산"을 빨간색으로 출력)
text = "아름다운 강산"
draw.text((200, 260), text, font=font, fill=(0, 0, 255, 0))  # (R, G, B) 값으로 빨간색 지정

# 6. 다시 Pillow 이미지를 OpenCV 이미지로 변환
img = np.array(img_pil)

cv2.imshow('letters', img)
cv2.waitKey(0)
cv2.destroyAllWindows()