import cv2
import numpy as np

# 读取灰度图像
img = cv2.imread('file\\SDUT.jpg', 0)

# 获取图像的行数和列数
rows, cols = img.shape

# 创建一个空列表，用于存放分解后的位平面
bit_planes = []

# 循环8次，分别提取每个位平面
for i in range(8):
    # 创建一个提取矩阵，其元素为2的i次方
    extractor = np.ones((rows, cols), dtype=np.uint8) * (2 ** i)
    # 将图像与提取矩阵进行按位与操作，得到第i个位平面的原始值
    bit_plane = cv2.bitwise_and(img, extractor)
    # 将原始值除以2的i次方，得到第i个位平面的二值值（0或1）
    bit_plane = bit_plane // (2 ** i)
    # 将二值值乘以255，得到第i个位平面的二值图像（0或255）
    bit_plane = bit_plane * 255
    # 将第i个位平面的二值图像添加到列表中
    bit_planes.append(bit_plane)

# 创建一个空数组，用于存放拼接后的图片
concat_img = np.zeros((rows * 4, cols * 4), dtype=np.uint8)

# 循环8次，分别将每个位平面拼接到对应的位置上
for i in range(8):
    # 计算当前位平面在拼接图片中的行索引和列索引范围
    row_start = (i // 4) * rows  # 行索引起点（含）
    row_end = row_start + rows  # 行索引终点（不含）
    col_start = (i % 4) * cols  # 列索引起点（含）
    col_end = col_start + cols  # 列索引终点（不含）

    # 将当前位平面复制到拼接图片中对应位置上
    concat_img[row_start:row_end, col_start:col_end] = bit_planes[i]

# 显示原始图像和拼接后的图片
# cv2.imshow('Original Image', img)
# cv2.imshow('Concatenated Image', concat_img)
cv2.imwrite('newfile\\concat.jpg', concat_img)


# 读取载体图像和水印图像
carrier = cv2.imread('file\\cameraman.jpg', 0) # 灰度图
watermark = cv2.imread('newfile\\concat.jpg', 0) # 二值图

# 将水印图像调整为与载体图像相同的大小
watermark = cv2.resize(watermark, (carrier.shape[1], carrier.shape[0]))

# 将水印图像转换为二进制数
_, watermark = cv2.threshold(watermark, 127, 255, cv2.THRESH_BINARY)
watermark = watermark // 255 # 将255变为1

# 将载体图像分解为8个位平面
bit_planes = []
for i in range(8):
    bit_plane = (carrier >> i) & 1 # 右移i位，与1进行按位与操作，得到第i个位平面
    bit_plane = bit_plane * 255 # 将1变为255，方便显示
    bit_planes.append(bit_plane)

# 将载体图像的最低有效位平面替换为水印信息，得到嵌入水印后的载体图像
bit_planes[0] = watermark * 255
carrier_with_watermark = np.zeros_like(carrier)
for i in range(8):
    carrier_with_watermark += bit_planes[i] * (2 ** i) # 按权相加，还原为灰度值

# 提取嵌入水印后的载体图像中的水印信息，得到提取出的水印信息
extracted_watermark = (carrier_with_watermark & 1) * 255 # 获取最低有效位平面，并将1变为255

# 显示结果
cv2.imshow('Carrier', carrier)
cv2.imshow('Watermark', watermark * 255)
cv2.imshow('Carrier with Watermark', carrier_with_watermark)
cv2.imshow('Extracted Watermark', extracted_watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()
