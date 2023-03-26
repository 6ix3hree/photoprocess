# # #no2.1各向异性扩散滤波
#
#
#
#
#
#
# # # no2.2双边滤波
# # # -*- coding: utf-8 -*-
# # # By:Eastmount
# # import cv2
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # # 读取图片
# # img = cv2.imread('file\\image.jpg')
# # source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #
# # # 双边滤波
# # result = cv2.bilateralFilter(source, 15, 150, 150)
# #
# # # 用来正常显示中文标签
# # plt.rcParams['font.sans-serif'] = ['SimHei']
# #
# # # 显示图形
# # titles = ['原始图像', '双边滤波']
# # images = [source, result]
# # for i in range(2):
# #     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
# #     plt.title(titles[i])
# #     plt.xticks([]), plt.yticks([])
# # plt.show()
#
#
#
# # no2.3引导式滤波器
# import cv2
# import numpy as np
# import itertools
#
# from core.filter import GuidedFilter
# from tools import visualize as vis
# from cv.image import to_8U, to_32F
#
#
#
# def test_gray():
#     image = cv2.imread('data/cat.png')
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     radius = [2, 4, 8]
#     eps = [0.1**2, 0.2**2, 0.4**2]
#
#     combs = list(itertools.product(radius, eps))
#
#     vis.plot_single(image, title='origin')
#     for r, e in combs:
#         GF = GuidedFilter(image, radius=r, eps=e)
#         vis.plot_single(GF.filter(image), title='r=%d, eps=%.2f' % (r, e))
#
#
# def test_color():
#     image = cv2.imread('data/Lenna.png')
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
#     noise = (np.random.rand(image.shape[0], image.shape[1], 3) - 0.5) * 50
#     image_noise = image + noise
#
#     radius = [1, 2, 4]
#     eps = [0.005]
#
#     combs = list(itertools.product(radius, eps))
#
#     vis.plot_single(to_32F(image), title='origin')
#     vis.plot_single(to_32F(image_noise), title='noise')
#
#     for r, e in combs:
#         GF = GuidedFilter(image, radius=r, eps=e)
#         vis.plot_single(to_32F(GF.filter(image_noise)), title='r=%d, eps=%.3f' % (r, e))
#
#
# if __name__ == '__main__':
#     test_gray()
#     test_color()
#
#
#
#
#
#
#
#
#
#
#

import  cv2
def bi_demo(image):#高斯双边滤波
    dst = cv2.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=15)
    cv2.namedWindow('bi_demo',0)
    cv2.resizeWindow('bi_demo',300,400)
    cv2.imshow("bi_demo", dst)

'''
    其中各参数所表达的意义：
    src：原图像；
    d：像素的邻域直径，可有sigmaColor和sigmaSpace计算可得；
    sigmaColor：颜色空间的标准方差，一般尽可能大；
    sigmaSpace：坐标空间的标准方差(像素单位)，一般尽可能小。'''

def mean_shift_demo(image):#均值偏移滤波
    dst = cv2.pyrMeanShiftFiltering(src=image, sp=15, sr=20)
    cv2.namedWindow('mean_shift image', 0)
    cv2.resizeWindow('mean_shift image', 300, 400)
    cv2.imshow("mean_shift image", dst)


#使用均值边缘保留滤波时，可能会导致图像过度模糊
'''其中各参数所表达的意义：
    src：原图像;
    sp：空间窗的半径(The spatial window radius);
    sr：色彩窗的半径(The color window radius)'''


src = cv2.imread('file\\image.jpg')
bi_demo(src)
mean_shift_demo(src)
cv2.namedWindow('src', 0)
cv2.resizeWindow('src', 300, 400)
cv2.imshow('src',src)
cv2.waitKey(0)