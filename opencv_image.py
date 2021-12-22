import cv2

# image 파일 읽기
img = cv2.imread('Scent.jpg')
img2 = cv2.resize(img, (600, 400))

# image 파일 읽기
cv2.imshow('Scent', img2)

edge = cv2.Canny(img, 50, 100)

# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

#열려있는 모든 창 닫기
cv2.destroyAllWindows()