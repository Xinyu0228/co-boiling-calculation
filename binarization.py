
import cv2
from scipy.signal import argrelmin
import numpy as np


def triangle_binarization(img_conv, save):
    print('converting to binary using Triangle binarization ...')
    for i in range(10):
        ret, img = cv2.threshold(img_conv.data[i], 0, 255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)
        img_conv.data.append(img)
        img_conv.colour_space.append(img_conv.colour_space[i] + '_trianglebin')
        if save:
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '_trianglebin.')
            if img_conv.colour_space[i][0] == 'o':
                cv2.imwrite(img_conv.path + img_conv.scenario +'processed/orig_gray/binary/' + name, img)
            elif img_conv.colour_space[i][0] == 'C':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                            img_conv.colour_space[i][1] + '/binary/' + name, img)
            else:
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] + '/binary/'
                            + name, img)
    return img_conv


def otsus_binarization(img_conv, save):
    print('converting to binary using Otsu`s binarization ...')
    for i in range(10):
        ret, img = cv2.threshold(img_conv.data[i], 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img_conv.data.append(img)
        img_conv.colour_space.append(img_conv.colour_space[i] + '_otsubin')
        if save:
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '_otsusbin.')
            if img_conv.colour_space[i][0] == 'o':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray/binary/' + name, img)
            elif img_conv.colour_space[i][0] == 'C':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                            img_conv.colour_space[i][1] + '/binary/' + name, img)
            else:
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] + '/binary/'
                            + name, img)
    return img_conv


def adaptive_mean_binarization(img_conv, save):
    print('converting to binary using adaptive threshold-mean method...')
    for i in range(10):
        for j in range(3, 13, 2):
            img_bin = cv2.adaptiveThreshold(img_conv.data[i], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, j, 0)
            img_conv.data.append(img_bin)
            img_conv.colour_space.append(img_conv.colour_space[i] + '_meanbin' + str(j))
            if save:
                name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '_meanbin' + str(j) + '.')
                if img_conv.colour_space[i][0] == 'o':
                    cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray/binary/' + name, img_bin)
                elif img_conv.colour_space[i][0] == 'C':
                    cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                                img_conv.colour_space[i][1] + '/binary/' + name, img_bin)
                else:
                    cv2.imwrite(
                        img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] + '/binary/' +
                        name, img_bin)
    return img_conv


def adaptive_gaussian_binarization(img_conv, save):
    print('converting to binary using adaptive threshold-gaussian method...')
    for i in range(10):
        for j in range(3, 13, 2):
            img_bin = cv2.adaptiveThreshold(img_conv.data[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, j,
                                            0)
            img_conv.data.append(img_bin)
            img_conv.colour_space.append(img_conv.colour_space[i] + '_gaussbin' + str(j))
            if save:
                name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '_gaussbin' + str(j) + '.')
                if img_conv.colour_space[i][0] == 'o':
                    cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray/binary/' + name, img_bin)
                elif img_conv.colour_space[i][0] == 'C':
                    cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                                img_conv.colour_space[i][1] + '/binary/' + name, img_bin)
                else:
                    cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                                '/binary/' + name, img_bin)
    return img_conv


def histogram_minima_binarization(img_conv, save, V_BAL):
    for i in range(10):
        histo = cv2.calcHist(img_conv.data, [i], None, [256], [0, 256])
        minima = argrelmin(histo)
        mini = minima[0]
        best_qc = 6
        for thresh in mini:
            img_bin = cv2.threshold(src=img_conv.data[i], thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
            height, width = img_bin.shape
            bp = 1 - (np.histogram(img_bin)[0][0] / (height * width))
            qc = abs(V_BAL - bp)
            if qc < best_qc:
                best_qc = qc
                best_thresh = thresh

        img = cv2.threshold(img_conv.data[i], best_thresh, 255, cv2.THRESH_BINARY)[1]
        img_conv.data.append(img)
        img_conv.colour_space.append(img_conv.colour_space[i] + '_minimabin')
        if save:
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i] + '_minimabin' + str(best_thresh)
                                         + '_' + format(best_qc, '.3g') + '.')
            if img_conv.colour_space[i][0] == 'o':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray/binary/' + name, img)
            elif img_conv.colour_space[i][0] == 'C':
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] +
                            img_conv.colour_space[i][1] + '/binary/' + name, img)
            else:
                cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i][0] + '/binary/'
                            + name, img)
    return img_conv
