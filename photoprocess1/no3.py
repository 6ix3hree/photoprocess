import cv2
import numpy as np

# 读入图像
img = cv2.imread('file\\image.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel算子横向处理
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel算子纵向处理
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 横向和纵向结果取绝对值并转换为8位图像
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# 将横向和纵向结果加权融合
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# 显示结果
cv2.imshow('sobel', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
