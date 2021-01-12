import cv2

img = cv2.imread("/home/kh/Pictures/hi/hi.jpeg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img_resize = cv2.resize(img,(500,250))

cv2.imshow("img_frame",img)
cv2.imshow("img_gray_frame",img_gray) # convert image to gray
cv2.imshow("img_hsv_frame",img_hsv) # convert image to hsv
cv2.imshow("img_resize_frame",img_resize) # resize image
cv2.waitKey(0)
