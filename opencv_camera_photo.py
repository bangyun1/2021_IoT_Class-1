import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    exit()

# 카메라 사진 찍기
ret, frame = cap.read()

cv2.imshow('frame', frame)
cv2.imwrite('output.jpg', frame)

cv2. waitKey(10000) # 어떤 키를 입력받으면 창이 닫히고 
#아무키도 입력 안하면 10초뒤 자동 닫힘

# 사용자 자원 해제
cap.release()
cv2.destroyAllWindows()