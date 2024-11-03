import cv2
from scipy.signal import argrelmin
import numpy as np
import subscripts.binarization
import numpy as np
import matplotlib.pyplot as plt
import os
import configparser
#是用来读取配置文件的包ConfigParser()
import copy
import subscripts.binarization
import subscripts.calculations
import subscripts.color_model_change_plot
import subscripts.monochromatic
import subscripts.organize_workspace
import subscripts.singleband_histo_sum_plots_ocv
import subscripts.spatially_illumination
import matplotlib

# x=np.arange(0,6,0.1)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()
#
#
# #打印opencv的版本号
# #print(cv2.__version__)
#
# def cv_show(name,img):
#     cv2.imshow("rabbit/rabbit.jpg", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# #读取、显示图像
img=cv2.imread("rabbit/rabbit.jpg")
# cv_show('rabbit/rabbit.jpg',img)
# #subscripts.singleband_histo_sum_plots_ocv.overview_plot(img)
# image_1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv_show('1',image_1)
# image_2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv_show('2',image_2)
# image_3 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
# cv_show('3',image_3)
#
# image_new_split = cv2.split(image_1)#将图像分为三个通道
# print(image_new_split)

# subscripts.singleband_histo_sum_plots_ocv.overview_plot(image_1)
#转化成为灰度图
#cv_show('rabbit/rabbit.jpg',img)

#截取图像的一部分
#rabbit=img[0:200,0:200]
#cv_show('rabbit/rabbit.jpg',rabbit)

#图像的数值计算，两个图像相加
#rabbit2=img+img
#cv_show('rabbit/rabbit.jpg',rabbit2)

#使用高斯滤波对图像进行处理
#aussian=cv2.GaussianBlur(img,(5,5),1)
#cv_show('rabbit/rabbit.jpg',aussian)

#展示所有的
#res=np.hstack((img,aussian))
#print(res)
#cv2.imshow('Grayscale vs Gaussian',res)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

 #梯度计算：提取图像的边缘
 #x方向
#sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
#sobelx=cv2.convertScaleAbs(sobelx)
#cv_show('sobelx',sobelx)
 #y方向
#sobely=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
#sobely=cv2.convertScaleAbs(sobelx)
#cv_show('sobely',sobely)
#sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#cv_show('sobelxy',sobelxy)

#Canny边缘检测算法
#v1=cv2.Canny(img,80,150)
#v2=cv2.Canny(img,50,100)
#res=np.hstack((v1,v2))
#cv_show('res',res)

#b,g,r=cv2.split(img)
#print(b)
#print(b.shape)
#print(g)
#print(r)

#只保留R通道
#cur_img=img.copy()
#cur_img[:,:,1]=0
#cur_img[:,:,2]=0
#cv_show('B',cur_img)

# import matplotlib.pyplot as plt
#
# # 定义图形
# fig = plt.figure()
# # 在布局中添加第一个子图，该布局具有3行和2列
# ax1 = fig.add_subplot(3,2,1)
# ax1.plot([1, 2, 3], [1, 2, 3])
#
# # 在布局中添加第五个子图，该布局具有3行和2列
# ax5 = fig.add_subplot(3,2,5)
# ax5.plot([1, 2, 3], [3, 2, 1])
#
# # 显示图形
# plt.show()


import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 定义一个图像类
class Image:
    def __init__(self, data, colour_space):
        self.data = data
        self.colour_space = colour_space

# 读取图像并创建图像对象
img = Image(cv2.imread("rabbit/rabbit.jpg"), str())

# 定义颜色模型
colour_model = ('RGB', 'HSV', 'YCbCr')

# 遍历颜色模型并转换图像颜色空间
for c in colour_model:
    # 创建图像并调整子图间距和字体大小
    fig = plt.figure(figsize=(15, 10))
    fig.subplots_adjust(hspace=0.3, wspace=0.5)
    matplotlib.rcParams.update({'font.size': 8})

    if c == 'RGB':
        print("c == 'RGB'")
        image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2RGB)  # 将BGR转换为RGB
        img.colour_space = 'R', 'G', 'B'
    if c == 'HSV':
        print("c == 'HSV'")
        image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2HSV)
        img.colour_space = 'H', 'S', 'V'
    if c == 'YCbCr':
        print("c == 'YCbCr'")
        image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2YCrCb)
        img.colour_space = 'Y', 'Cr', 'Cb'

    # 显示原始图像和转换后的图像
    sp_orig = fig.add_subplot(3, 4, 1)
    sp_orig.imshow(cv2.cvtColor(img.data, cv2.COLOR_BGR2RGB))
    sp_orig.axis('off')
    sp_orig.set_title('original')


    # 分离图像通道并计算直方图最大值
    img_split = cv2.split(image_new)
    max_y = 0
    for b in img_split:
        max_hist = max(cv2.calcHist([b], [0], None, [256], [0, 256]))  # 计算直方图并找最大值
        # 五个参数为图像、通道、掩码、直方图大小和像素值范围
        if max_y < max_hist:
            max_y = max_hist

    # 遍历每个通道并显示单通道图像和直方图
    for i in range(0, 3, 1):
        sp_single_band = fig.add_subplot(3, 4, (2 + i))
        sp_single_band.imshow(img_split[i], cmap='gray')
        sp_single_band.axis('off')
        sp_single_band.set_title(img.colour_space[i])

        histo = cv2.calcHist([img_split[i]], [0], None, [256], [0, 256])
        histo_arr = np.array(histo)
        sp_histo = fig.add_subplot(3, 4, (6 + i))
        sp_histo.plot(histo)
        sp_histo.axis([-10, 256, 0, max_y + max_y * 0.1])

        # 计算累积和并绘制累积和曲线
        sum_value = np.zeros(histo_arr.shape)
        for j in range(histo_arr.shape[0]):
            sum_value[j] = histo_arr[j] + sum_value[j - 1]
        x = np.arange(histo_arr.shape[0])
        sp_sum = fig.add_subplot(3, 4, (10 + i))
        sp_sum.plot(x, sum_value)

        if i == 0:
            plt.yscale('log')

    plt.show()


