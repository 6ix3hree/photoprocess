# 导入OpenCV库
import cv2

# 读取一幅彩色图像，并将它调整为512x512像素，24位每像素三通道
img = cv2.imread('file\\cameraman.jpg')
img = cv2.resize(img, (512, 512))

# 显示彩色图像
cv2.imshow('Color Image', img)

# 分离图像的三个通道
b, g, r = cv2.split(img)

# 显示三个通道灰度图
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# 交换GRB通道后重组新图像，比如R-〉G，G-〉B，B-〉R
new_img = cv2.merge((r, b, g))

# 显示新图像
cv2.imshow('New Image', new_img)

# 输出保存图像
cv2.imwrite('result.jpg', new_img)

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()