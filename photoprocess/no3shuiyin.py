# 导入opencv库
import cv2

# 读取图像文件
img = cv2.imread('file\\image.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 直方图均衡化
equ = cv2.equalizeHist(gray)

# 获得灰度转换函数
cdf = equ.cumsum() # 累积频率
cdf_normalized = cdf * 255 / cdf[-1] # 归一化
lut = cdf_normalized.astype("uint8") # 映射表

# 识别水印（假设水印在右下角）
h, w = gray.shape # 图像高和宽
roi = gray[h-100:h, w-100:w] # 感兴趣区域
ret, mask = cv2.threshold(roi, 200, 255, cv2.THRESH_BINARY) # 阈值分割
watermark = cv2.bitwise_and(roi, mask) # 按位与操作

# 显示结果
cv2.imshow("Original", img)
cv2.imshow("Equalized", equ)
# cv2.imshow("Watermark", watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()