import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()
now_str = time.strftime("%Y%m%d_%H%M%S")

try:
    while True:
        val = input("photo :1, video:2, exit:9 >")
        if val == '1':
            print("\n사진 촬영")
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)   #카메라 촬영 시 준비시간 필요              #사진
            camera.rotation = 180                                  #사진
            camera.capture('%s/photo_%s.jpg' % (path, now_str))                  #사진 촬영
        elif val == '2':
            print("\n동영상 촬영")
            camera.start_recording('%s/video_%s.h264' % (path, now_str))          #동영상 촬영
            input('press enter to stop')                            #엔터 누를 때까지 동영상
            time.sleep(10)                                         #동영상 10초
            camera.stop_recording()                                 #동영상
        elif val == '9':
            print("\n종료")
            break
finally:
    camera.stop_preview()