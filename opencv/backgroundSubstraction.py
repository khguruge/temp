import cv2
import numpy as np

cap = cv2.VideoCapture("/home/kh/Videos/4K Video Downloader/highway.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
_, first_frame = cap.read();
_, mask = cap.read();

while True:
    _, frame = cap.read();
    mask = subtractor.apply(frame);
    # difference = cv2.absdiff(first_frame, frame);
    # cv2.imshow("First_frame", first_frame)
    cv2.imshow("Frame", frame);
    # cv2.imshow("difference", difference);
    cv2.imshow("mask", mask)

    key = cv2.waitKey(30);
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()