import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    #time.sleep(3) #카메라 촬영 시 준비시간 필요              #사진
    #camera.rotation = 180                                  #사진
    #camera.capture('%s/photo.jpg' % path)                  #사진 촬영
    camera.start_recording('%s/video.h264' % path)          #동영상 촬영
    input('press enter to stop')                            #엔터 누를 때까지 동영상
    #time.sleep(10)                                         #동영상 10초
    camera.stop_recording()                                 #동영상

finally:
    camera.stop_preview()