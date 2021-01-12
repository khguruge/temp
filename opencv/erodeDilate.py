import cv2

img = cv2.imread("/home/kh/Pictures/hi/hi.jpeg")
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img_resize = cv2.resize(img,(500,250))

cv2.imshow("helllo",img)

cv2.waitKey(0)




# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('/home/kh/Documents/temp/opencv/smarties.png', cv2.IMREAD_GRAYSCALE)

# cv2.imshow("helllo",img)
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# kernal = np.ones((5,5), np.uint8)

# dilation = cv2.dilate(mask, kernal, iterations=2)
# erosion = cv2.erode(mask, kernal, iterations=1)
# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
# th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

# titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
# images = [img, mask, dilation, erosion, opening, closing, mg, th]

# for i in range(8):
#     plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()