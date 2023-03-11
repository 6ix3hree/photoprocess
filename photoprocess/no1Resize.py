# 导入OpenCV库
import cv2
import numpy as np
# 读取两幅实验图像，并将它们调整为256x256像素，8位每像素
img1 = cv2.imread('file\\cameraman.jpg',cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (256, 256))
img2 = cv2.imread('file\\lena.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, (256, 256))

# 显示两幅图像
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)

# 定义一幅新图像，使新图像的左半部分和1相同，右半部分和2相同
new_img = np.zeros((256, 256), dtype=np.uint8) # 创建一个空白的256x256的8位无符号整数数组
new_img[:, :128] = img1[:, :128]
new_img[:, 128:] = img2[:, 128:]

# 显示新图像
cv2.imshow('New Image', new_img)

# 定义一幅新图像对B的结果进行左右反转
flipped_img = cv2.flip(new_img, 1)

# 显示反转后的图像
cv2.imshow('Flipped Image', flipped_img)

# 定义一幅新图像对C的结果进行反片处理，D=255-C
inverted_img = cv2.bitwise_not(flipped_img)

# 显示反片后的图像
cv2.imshow('Inverted Image', inverted_img)

# 输出保存D结果为TIF和JPEG格式
cv2.imwrite('newfile\\result.tif', inverted_img)
cv2.imwrite('newfile\\result.jpg', inverted_img)

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()