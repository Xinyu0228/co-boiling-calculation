
import matplotlib.pyplot as plt
import matplotlib
import cv2
import numpy as np


def overview_plot(img):

    print('Plotting an overview plot for RGB, HSV and YCbCr including histogram...')
    # converting to HSV and YCbCr
    colour_model = ('RGB', 'HSV', 'YCbCr')
    for c in colour_model:
        fig = plt.figure(figsize=(15, 10))
        fig.subplots_adjust(hspace=0.3, wspace=0.5)
        matplotlib.rcParams.update({'font.size': 8})

        if c == 'RGB':
            # print("c == 'RGB")
            image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2RGB)
            img.colour_space = 'R', 'G', 'B'
        if c == 'HSV':
            # print("c == 'HSV")
            image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2HSV)
            img.colour_space = 'H', 'S', 'V'
        if c == 'YCbCr':
            # print("c == 'YCbCr")
            image_new = cv2.cvtColor(img.data, cv2.COLOR_BGR2YCrCb)
            img.colour_space = 'Y', 'Cr', 'Cb'


        sp_orig = fig.add_subplot(3, 4, 1)
        sp_orig.imshow(cv2.cvtColor(img.data, cv2.COLOR_BGR2RGB))
        sp_orig.axis('off')
        sp_orig.set_title('original')


        image_new_split = cv2.split(image_new)
        max_y = 0
        for b in image_new_split:
            max_hist = max(cv2.calcHist([b], [0], None, [256], [0, 256]))
            if max_y < max_hist:
                max_y = max_hist



        for i in range(0, 3, 1):
            sp_single_band = fig.add_subplot(3, 4, (2 + i))
            sp_single_band.imshow(image_new_split[i], cmap='gray')
            sp_single_band.axis('off')
            sp_single_band.set_title(img.colour_space[i])


            histo = cv2.calcHist([image_new_split[i]], [0], None, [256], [0, 256])
            histo_arr = np.array(histo)
            sp_histo = fig.add_subplot(3, 4, (6 + i))
            sp_histo.plot(histo)
            sp_histo.axis([-10, 256, 0, max_y + max_y * 0.1])



            sum_value = np.zeros(histo_arr.shape)
            for j in range(histo_arr.shape[0]):
                sum_value[j] = histo_arr[j] + sum_value[j - 1]
            x = np.arange(histo_arr.shape[0])
            sp_sum = fig.add_subplot(3, 4, (10 + i))
            sp_sum.plot(x, sum_value)


            if i == 0:
                plt.yscale('log')#y
                sp_sum.set_title('sum curve ' + img.colour_space[i] + ', log')
            elif i == 1:
                plt.yscale('symlog')
                sp_sum.set_title('sum curve ' + img.colour_space[i] + ', symlog')
            else:
                plt.yscale('linear')
                sp_sum.set_title('sum curve ' + img.colour_space[i] + ', linear')
            sp_sum.set_xlabel('grey level')
            sp_sum.set_ylabel('pixel sum')

            new_name = img.name.replace('.', '_' + c + '.')
            fig.savefig(img.path + img.scenario + 'post_processing/poly_plot/' + new_name)
    plt.show()
    plt.close()









