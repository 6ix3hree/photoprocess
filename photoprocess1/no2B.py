import cv2

# 读取图像
img = cv2.imread('file\\image.jpg')

# 双边滤波
filtered = cv2.bilateralFilter(img, 9, 75, 75)

# 显示原图和滤波后的图像
cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
