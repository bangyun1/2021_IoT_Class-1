import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D' ,'O' ,'V' ,'X')
# fourcc(four character code): DIVX(avi), MP4V(mp4), X264(h264)

# 동영상 저장을 위한 VideoWriter 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))
#cv2.VideoWriter('<저장할 파일명>.avi', fourcc, <초당 프레임>, (<프레임 사이즈>))

while True:
    ret, frame = cap.read()
    edge = cv2.Canny(frame, 150, 200)
    cv2.imshow('edge1', edge)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray', gray)
    if not ret:
        break
    
    cv2.imshow('frame', frame)
    out.write(frame)

    if cv2.waitKey(10) == 27: #27은 ESC
        break

# 사용자 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()