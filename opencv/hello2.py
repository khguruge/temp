
import cv2

cap = cv2.VideoCapture("/home/kh/Videos/4K Video Downloader/Kuweni - Cover by Reeni de Silva.mp4")
# 0 is used to connect your webcam
# 1,2 may used when you use another usb web camera
# if you use IP camera (like CCTV) cap = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')
# id you need read video in your pc, cap = cv2.VideoCapture("/home/nuwan/vide_name.mp4")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame",frame)
        cv2.waitKey(1)

