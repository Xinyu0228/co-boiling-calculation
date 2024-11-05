
import cv2
import copy


def conversion_to_grayscale(img, save):
    print('converting to gray scale image...')
    img_conv = copy.deepcopy(img)
    img_conv.data = [cv2.cvtColor(img_conv.data, cv2.COLOR_BGR2GRAY)]
    img_conv.colour_space = ['orig_gray']
    if save is True:
        name = img_conv.name.replace('.', '_' + img_conv.colour_space[0] + '.')
        cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/orig_gray/orig_gray/' + name, img_conv.data[0])
    return img_conv


def split_RGB(img, img_conv, save):
    print('splitting RGB into single bands...')
    img_conv.data.extend(cv2.split(cv2.cvtColor(img.data, cv2.COLOR_BGR2RGB)))
    img_conv.colour_space.extend('RGB')
    if save:
        for i in range(3):
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i + 1] + '.')
            cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i + 1] + '/' +
                        img_conv.colour_space[i + 1] + '/' + name, img_conv.data[i + 1])
    return img_conv


def conversion_to_HSV(img, img_conv, save):
    print('converting to HSV and splitting...')
    img_conv.data.extend(cv2.split(cv2.cvtColor(img.data, cv2.COLOR_BGR2HSV)))
    img_conv.colour_space.extend('HSV')
    if save:
        for i in range(3):
            name = img_conv.name.replace('.', '_' + img_conv.colour_space[i+4] + '.')
            cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + img_conv.colour_space[i+4] + '/' +
                        img_conv.colour_space[i+4] + '/' + name, img_conv.data[i+4])
    return img_conv


def conversion_to_YCbCr(img, img_conv, save):
    print('converting to YCbCr and splitting...')
    img_conv.data.extend(cv2.split(cv2.cvtColor(img.data, cv2.COLOR_BGR2YCrCb)))
    img_conv.colour_space.append('Y')
    img_conv.colour_space.append('Cr')
    img_conv.colour_space.append('Cb')
    if save:
        for i in range(3):
            name = img_conv.name.replace('.', '_' + str(img_conv.colour_space[i+7]) + '.')
            cv2.imwrite(img_conv.path + img_conv.scenario + 'processed/' + str(img_conv.colour_space[i+7]) + '/' +
                        str(img_conv.colour_space[i+7]) + '/' + name, img_conv.data[i+7])

    return img_conv


