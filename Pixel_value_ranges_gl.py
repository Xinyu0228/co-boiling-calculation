from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('data/tutori/tutorial/single_pic/PIC/XXX.tif')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


fig = plt.figure()


plt.imshow(img_rgb)


click_count = 0
pixel_values_rgb = []
pixel_values_ycbcr = []
pixel_values_hsv = []

def onclick(event):
    global click_count, pixel_values_rgb, pixel_values_ycbcr, pixel_values_hsv


    x = int(event.xdata)
    y = int(event.ydata)


    pixel_value_rgb = img_rgb[y, x]
    pixel_value_ycbcr = img_ycbcr[y, x]
    pixel_value_hsv = img_hsv[y, x]
    print(f'Pixel value at ({x}, {y}):')
    print(f'RGB={pixel_value_rgb}')



    pixel_values_rgb.append(pixel_value_rgb)
    pixel_values_ycbcr.append(pixel_value_ycbcr)
    pixel_values_hsv.append(pixel_value_hsv)
    click_count += 1


    if click_count == 100:
        min_pixel_value_rgb = np.min(pixel_values_rgb, axis=0)
        max_pixel_value_rgb = np.max(pixel_values_rgb, axis=0)
        min_pixel_value_ycbcr = np.min(pixel_values_ycbcr, axis=0)
        max_pixel_value_ycbcr = np.max(pixel_values_ycbcr, axis=0)
        min_pixel_value_hsv = np.min(pixel_values_hsv, axis=0)
        max_pixel_value_hsv = np.max(pixel_values_hsv, axis=0)
        print(f'The range of pixel values is:')
        print(f'RGB: {min_pixel_value_rgb} - {max_pixel_value_rgb}')
        print(f'YCbCr: {min_pixel_value_ycbcr} - {max_pixel_value_ycbcr}')
        print(f'HSV: {min_pixel_value_hsv} - {max_pixel_value_hsv}')


cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
