# import cv2
#
# # 加载图像
# image = cv2.imread('file\\image.jpg')
#
# # 将图像转换为灰度
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # 应用各向异性扩散滤波器
# filtered = cv2.edgePreservingFilter(gray, flags=cv2.RECURS_FILTER)
#
# # 显示结果
# cv2.imshow('Filtered Image', filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
img = cv2.imread('file\\image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0.0625, 0.125, 0.0625],
                   [0.125,  0.25,  0.125],
                   [0.0625, 0.125, 0.0625]])
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('应用各向异性扩散滤波器',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()