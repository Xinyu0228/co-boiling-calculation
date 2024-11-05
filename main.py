
## NAPL Removal Quantification Tool during Co-boiling
## This repository contains code used to quantify the removal of NAPL (Non-Aqueous Phase Liquid) and to establish the relationship between NAPL removal and the temperature field. This code is adapted from the methodologies and research findings presented in several academic papers.

## Acknowledgements
## This code is provided as a tool for research purposes and is based on the methodologies described in the referenced papers. It is not intended to be an original contribution but rather a practical implementation of existing research. It is adapted from the methodologies and research findings presented in the following papers:

## Engelmann, C.; Lari, K. S.; Schmidt, L.; Werth, C. J.; Walther, M. Towards predicting DNAPL source zone formation to improve plume assessment: using robust laboratory and numerical experiments to evaluate the relevance of retention curve characteristics. Journal of Hazardous Materials 2021, 407, 124741. DOI: 10.1016/j.jhazmat.2020.124741.
## Kechavarzi, C.; Soga, K.; Wiart, P. Multispectral image analysis method to determine dynamic fluid saturation distribution in two-dimensional three-fluid phase flow laboratory experiments. Journal of Contaminant Hydrology 2000, 46 (3-4), 265-293. DOI: 10.1016/s0169-7722(00)00133-9.
## Engelmann, C.; Schmidt, L.; Werth, C. J.; Walther, M. Quantification of Uncertainties from Image Processing and Analysis in Laboratory-Scale DNAPL Release Studies Evaluated by Reflective Optical Imaging. Water 2019, 11 (11), 2274. DOI: 10.3390/w11112274.
## Belfort, B. M.; Weill, S.; Lehmann, F. Image analysis method for the measurement of water saturation in a two-dimensional experimental flow tank. Journal of Hydrology 2017, 550, 343-354. DOI: 10.1016/j.jhydrol.2017.05.007.
## Alazaiza, M. Y. D.; Ramli, M. H.; Copty, N. K.; Ling, M. C. Assessing the impact of water infiltration on LNAPL mobilization in sand column using simplified image analysis method. Journal of Contaminant Hydrology 2021, 238, 103769. DOI: 10.1016/j.jconhyd.2021.103769.


import os
import cv2
import configparser
import copy
import subscripts.binarization
import subscripts.calculations
import subscripts.color_model_change_plot
import subscripts.monochromatic
import subscripts.organize_workspace
import subscripts.singleband_histo_sum_plots_ocv
import subscripts.spatially_illumination


#-- config *.ini file --------
config = configparser.ConfigParser(allow_no_value=True,
                                   converters={'list': lambda x: [i.strip() for i in x.split(',')]})

config.read('scenarios/tutorial.ini')
START_LEFT = config.getint('Crop Values', 'S_L')
START_TOP = config.getint('Crop Values', 'S_T')
END_RIGHT = config.getint('Crop Values', 'E_R')
END_BOTTOM = config.getint('Crop Values', 'E_B')
V_BAL = config.getfloat('Volume Balance', 'V_BAL')



ipa_sequence = []
for key in config['IPA steps']:
    ipa_sequence.append(config['IPA steps'].getlist(key))


plots = []
for key in config['plots']:
    plots.append(key)


class SinglePicture(object):

    def __init__(self, path, scenario, source_folder, name):
        self.path = path
        self.scenario = scenario
        self.source_folder = source_folder
        self.name = name
        self.data = ()
        self.colour_space = str()
        self.qc = []



def run():
    path = 'data/tutori/tutorial/'
    scenario = 'single_pic/'
    source_folder = 'TIFF/'
    subscripts.organize_workspace.workspace(path=path, scenario=scenario)
    list_images = os.listdir(path + scenario + source_folder) #list_images
    print(list_images)

    for i in range(len(list_images)):
        print('Reading original image ' + str(i + 1) + ' of ' + str(len(list_images)) + '...')
        name = list_images[i]
        img = SinglePicture(path=path, scenario=scenario, source_folder=source_folder, name=name)
        img.data = cv2.imread(path + scenario + source_folder + name)


        # -- IP--
        for k in range(len(ipa_sequence)):
            # -- Crop image
            save = False
            if ipa_sequence[k][0] == 'crop':
                if ipa_sequence[k][1] == 's':
                    save = True
                img = subscripts.calculations.crop(img, save, START_LEFT, END_RIGHT, START_TOP, END_BOTTOM) #裁剪

            if ipa_sequence[k][0] == 'conv':
                if ipa_sequence[k][1] == 's':
                    save = True
                img_conv = subscripts.monochromatic.conversion_to_grayscale(img=img, save=save)
                img_conv = subscripts.monochromatic.split_RGB(img=img, img_conv=img_conv, save=save)
                img_conv = subscripts.monochromatic.conversion_to_HSV(img=img, img_conv=img_conv, save=save)
                img_conv = subscripts.monochromatic.conversion_to_YCbCr(img=img, img_conv=img_conv, save=save)


            # -- Calculate difference
            if ipa_sequence[k][0] == 'diff':
                if i == 0: 
                    img_ref = img_conv
                else:
                    if ipa_sequence[k][1] == 's':
                        save = True
                    img_conv = subscripts.calculations.calculate_difference(img_conv=img_conv, img_ref=img_ref,
                                                                            save=save)



            # -- binary --
            if ipa_sequence[k][0] == 'otsus_binary':
                if ipa_sequence[k][1] == 's':
                    save = True
                if i == 1:
                    img_bin = subscripts.binarization.otsus_binarization(img_conv=img_conv, save=save)


            if ipa_sequence[k][0] == 'triangle_binary':
                if ipa_sequence[k][1] == 's':
                    save = True
                if i == 1:
                    img_bin = subscripts.binarization.triangle_binarization(img_conv=img_conv, save=save)


            if ipa_sequence[k][0] == 'mean_binary':
                if ipa_sequence[k][1] == 's':
                    save = True
                if i == 1:
                    img_bin = subscripts.binarization.adaptive_mean_binarization(img_conv=img_conv, save=save)


            if ipa_sequence[k][0] == 'gauss_binary':
                if ipa_sequence[k][1] == 's':
                    save = True
                if i == 1:
                    img_bin = subscripts.binarization.adaptive_gaussian_binarization(img_conv=img_conv, save=save)


            if ipa_sequence[k][0] == 'minima_binary':
                if ipa_sequence[k][1] == 's':
                    save = True
                if i == 1:
                    img_bin = subscripts.binarization.histogram_minima_binarization(img_conv=img_conv, save=save,
                                                                                    V_BAL=V_BAL)


            if ipa_sequence[k][0] == 'calc_sat':
                if ipa_sequence[k][1] == 'n':
                    save = True
                if i == 1:
                    img_sat = subscripts.calculations.calculate_saturation(img_bin=img_bin, save=save)
                    print(img_sat)



            if ipa_sequence[k][0] == 'qc_v_bal':
                if ipa_sequence[k][1] == 'n':
                    save = True
                if i == 1:
                    img_bin = subscripts.calculations.quality_criteria_v_bal(img_bin=img_bin, save=save)


        for p in range(len(plots)):


            if plots[p] == 'single_band_histogram_sumcurve':
                cv2.imshow("Demo1", img.data)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                subscripts.singleband_histo_sum_plots_ocv.overview_plot(img)



    if i>=1:
        print('finished.')
    return 0


if __name__ == '__main__':
    success = run()
