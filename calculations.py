
# -- Module import --
import cv2
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
import os
import configparser
import pandas as pd

##裁剪流程函数
def crop(img, save, S_L, E_R, S_T, E_B):
    print('Cropping image...')
    img.data = img.data[S_T:E_B, S_L:E_R]
    if save:
        cv2.imwrite(img.path + img.scenario + 'processed/cropped/' + img.name, img.data)#保存裁剪后的数据
        print('Crops the image to area of interest, finished')
    return img


def calculate_difference(img_conv, img_ref, save):
    print('calculating difference of  first image...')
    for i in range(10):
        img_conv.data[i] = cv2.absdiff(img_ref.data[i], img_conv.data[i])
        img_conv.colour_space[i] = img_conv.colour_space[i] + '_absdiff'
        if save:
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '.')
            hist = cv2.calcHist(img_conv.data, [i], None, [256], [0, 256])
            plt.figure(figsize=(15, 7))  #15x7
            plt.plot(hist) #plot
            plt.title('histogram' + img_conv.scenario + img_conv.colour_space[i])
            plt.tight_layout()
            #Save
            if img_conv.colour_space[i][0] == 'o': 
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray' + '/diff/' + name,
                            img_conv.data[i])#save
                plt.savefig(img_conv.path + img_conv.scenario + 'post_processing/histograms/' +
                            img_conv.colour_space[i][0] + img_conv.colour_space[i][1] + '.png', dpi=300)
            elif img_conv.colour_space[i][0] == 'C':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                            img_conv.colour_space[i][1] + '/diff/' + name, img_conv.data[i])
                plt.savefig(img_conv.path + img_conv.scenario + 'post_processing/histograms/' +
                            img_conv.colour_space[i][0] + img_conv.colour_space[i][1] + '.png', dpi=300)

            else:
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] + '/diff/' +
                            name, img_conv.data[i])
                plt.savefig(img_conv.path + img_conv.scenario + 'post_processing/histograms/' +
                            img_conv.colour_space[i][0] + '.png', dpi=300)
            plt.close()
    return img_conv


def calculate_saturation(img_bin, save):
    print('calculating saturation distribution...')
    for i in range(10, len(img_bin.data), 1):
        img = img_bin.data[i]
        height, width = img.shape
        x_matrix = int(height / 15)
        y_matrix = int(width / 15)

        s = np.zeros((x_matrix, y_matrix), dtype=float) # size x_matrix, y_matrix
        cell_h = []
        cell_w = []
        for z in range(0, 15, 1):
            cell_h.append(z)
            cell_w.append(z)

        for x in range(x_matrix):
            for y in range(y_matrix):
                for h in cell_h:
                    for k in cell_w:
                        if img[x * 15 + h, y * 15 + k] == 0:
                            s[x, y] += 1
                        else:
                            s[x, y] += 0

        bp = 0
        for x in range(x_matrix):
            for y in range(y_matrix):
                bp += s[x, y]

        for x in range(x_matrix):
            for y in range(y_matrix):
                s[x, y] = 1 - (s[x, y] / (15 * 15))

        col_plot = cm.get_cmap('seismic', 225)
        plotcmp = col_plot(np.linspace(0.5, 1, 225))
        barcmp = ListedColormap(col_plot(np.linspace(0.52, 1, 225)))
        white = np.array([1, 1, 1, 1])
        plotcmp[:1, :] = white
        newcmp = ListedColormap(plotcmp)

        im = plt.imshow(s, cmap=barcmp, interpolation=None, vmin=0, vmax=1)
        plt.contourf(s, cmap=newcmp)
        clb = plt.colorbar(im)
        clb.ax.set_title('$\it{S}_{NW}$ (-)')
        plt.axis('off')

        name = img_bin.name.replace('.tif', img_bin.colour_space[i] + '_sat')


        if save:
            if img_bin.colour_space[i][0] == 'o':
                plt.savefig(img_bin.path + img_bin.scenario + 'processed/orig_gray/saturation/' + name + '.png',
                            dpi=300)


            elif img_bin.colour_space[i][0] == 'C':
                plt.savefig(img_bin.path + img_bin.scenario + 'processed/' + img_bin.colour_space[i][0] +
                            img_bin.colour_space[i][1] + '/saturation/' + name + '.png', dpi=300)


            else:
                plt.savefig(img_bin.path + img_bin.scenario + 'processed/' + img_bin.colour_space[i][0] + '/saturation/'
                            + name + '.png', dpi=300)


        plt.close()



def quality_criteria_v_bal(img_bin, save):
    for i in range(10, len(img_bin.data), 1):
        img = img_bin.data[i]
        height, width = img.shape
        wp = np.histogram(img, bins=2)[0][1] / (height * width)

        if wp == 1 and img_bin.data[i][0][0] == 0:
            wp = 0
            img_bin.qc.append(wp)

        if save:
            file_path = img_bin.path + img_bin.scenario + 'post_processing/quality_criteria/quality_criteria_vbal_' + str(
                img_bin.name) + '.txt'
            with open(file_path, 'a') as file:
                file.write(f'{img_bin.colour_space[i]},{wp}\n')

    return img_bin
