import cv2
import numpy as np

# 图像平滑是一种图像处理的操作，它可以减少图像中的噪声和细节，使图像看起来更平滑和柔和。平滑操作是通过将一个滤波器（也叫做核）应用到图像上实现的。
# 滤波器是一个小的矩阵，它包含了一些系数。滤波器在图像上移动时，会对每个像素及其邻域进行一些计算，然后用计算结果替换原来的像素值。
#
# KNN平滑滤波器是一种非线性的滤波器，它不是用固定的系数来计算输出像素值，而是根据输入像素与其邻域像素之间的灰度差异来选择最相似的K个邻居，并用这K个邻居的灰度均值作为输出像素值。
# 这样可以保留图像中的边缘和纹理信息，同时去除噪声。
# Read image
img = cv2.imread('file\\image1.jpg', cv2.IMREAD_GRAYSCALE)

# Define parameters
m = 3 # Size of the template
K = 5 # Number of nearest neighbors

# Pad image with zeros
pad = m // 2
img_pad = np.pad(img, pad_width=pad, mode='constant', constant_values=0)

# Create output image
img_out = np.zeros_like(img)

# Loop over each pixel
for i in range(pad, img_pad.shape[0] - pad):
    for j in range(pad, img_pad.shape[1] - pad):
        # Get template around pixel
        template = img_pad[i-pad:i+pad+1, j-pad:j+pad+1]
        # Flatten template into a vector
        template_vec = template.flatten()
        # Get pixel value
        pixel = img_pad[i,j]
        # Compute absolute difference between pixel and template vector
        diff = np.abs(template_vec - pixel)
        # Find indices of K smallest elements in diff array
        idx = np.argpartition(diff, K)[:K]
        # Get corresponding values from template vector
        values = template_vec[idx]
        # Compute mean of values as new pixel value
        mean_value = np.mean(values)
        # Assign mean value to output image at same location as pixel
        img_out[i-pad,j-pad] = mean_value

# Show output image
cv2.imshow('Output', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()