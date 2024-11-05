
import os


def workspace(path, scenario):
    # -- cropped --
    if not os.path.exists(path + scenario + 'processed/cropped'):
        os.makedirs(path + scenario + 'processed/cropped')
    # -- originally gray --
    if not os.path.exists(path + scenario + 'processed/orig_gray/orig_gray'):
        os.makedirs(path + scenario + 'processed/orig_gray/orig_gray')
    # diff / bw / sat
    if not os.path.exists(path + scenario + 'processed/orig_gray/diff'):
        os.makedirs(path + scenario + 'processed/orig_gray/diff')
    if not os.path.exists(path + scenario + 'processed/orig_gray/binary'):
        os.makedirs(path + scenario + 'processed/orig_gray/binary')
    if not os.path.exists(path + scenario + 'processed/orig_gray/saturation'):
        os.makedirs(path + scenario + 'processed/orig_gray/saturation')

    # -- RGB --
    if not os.path.exists(path + scenario + 'processed/R/R'):
        os.makedirs(path + scenario + 'processed/R/R')
    if not os.path.exists(path + scenario + 'processed/G/G'):
        os.makedirs(path + scenario + 'processed/G/G')
    if not os.path.exists(path + scenario + 'processed/B/B'):
        os.makedirs(path + scenario + 'processed/B/B')
    # diff / bw / sat
    if not os.path.exists(path + scenario + 'processed/R/diff'):
        os.makedirs(path + scenario + 'processed/R/diff')
    if not os.path.exists(path + scenario + 'processed/R/binary'):
        os.makedirs(path + scenario + 'processed/R/binary')
    if not os.path.exists(path + scenario + 'processed/R/saturation'):
        os.makedirs(path + scenario + 'processed/R/saturation')
    if not os.path.exists(path + scenario + 'processed/G/diff'):
        os.makedirs(path + scenario + 'processed/G/diff')
    if not os.path.exists(path + scenario + 'processed/G/binary'):
        os.makedirs(path + scenario + 'processed/G/binary')
    if not os.path.exists(path + scenario + 'processed/G/saturation'):
        os.makedirs(path + scenario + 'processed/G/saturation')
    if not os.path.exists(path + scenario + 'processed/B/diff'):
        os.makedirs(path + scenario + 'processed/B/diff')
    if not os.path.exists(path + scenario + 'processed/B/binary'):
        os.makedirs(path + scenario + 'processed/B/binary')
    if not os.path.exists(path + scenario + 'processed/B/saturation'):
        os.makedirs(path + scenario + 'processed/B/saturation')

    # -- HSV --
    if not os.path.exists(path + scenario + 'processed/H/H'):
        os.makedirs(path + scenario + 'processed/H/H')
    if not os.path.exists(path + scenario + 'processed/S/S'):
        os.makedirs(path + scenario + 'processed/S/S')
    if not os.path.exists(path + scenario + 'processed/V/V'):
        os.makedirs(path + scenario + 'processed/V/V')
    # diff / bw / sat
    if not os.path.exists(path + scenario + 'processed/H/diff'):
        os.makedirs(path + scenario + 'processed/H/diff')
    if not os.path.exists(path + scenario + 'processed/H/binary'):
        os.makedirs(path + scenario + 'processed/H/binary')
    if not os.path.exists(path + scenario + 'processed/H/saturation'):
        os.makedirs(path + scenario + 'processed/H/saturation')
    if not os.path.exists(path + scenario + 'processed/S/diff'):
        os.makedirs(path + scenario + 'processed/S/diff')
    if not os.path.exists(path + scenario + 'processed/S/binary'):
        os.makedirs(path + scenario + 'processed/S/binary')
    if not os.path.exists(path + scenario + 'processed/S/saturation'):
        os.makedirs(path + scenario + 'processed/S/saturation')
    if not os.path.exists(path + scenario + 'processed/V/diff'):
        os.makedirs(path + scenario + 'processed/V/diff')
    if not os.path.exists(path + scenario + 'processed/V/binary'):
        os.makedirs(path + scenario + 'processed/V/binary')
    if not os.path.exists(path + scenario + 'processed/V/saturation'):
        os.makedirs(path + scenario + 'processed/V/saturation')

    # -- YCbCr --
    if not os.path.exists(path + scenario + 'processed/Y/Y'):
        os.makedirs(path + scenario + 'processed/Y/Y')
    if not os.path.exists(path + scenario + 'processed/Cb/Cb'):
        os.makedirs(path + scenario + 'processed/Cb/Cb')
    if not os.path.exists(path + scenario + 'processed/Cr/Cr'):
        os.makedirs(path + scenario + 'processed/Cr/Cr')
    # diff / bw / sat
    if not os.path.exists(path + scenario + 'processed/Y/diff'):
        os.makedirs(path + scenario + 'processed/Y/diff')
    if not os.path.exists(path + scenario + 'processed/Y/binary'):
        os.makedirs(path + scenario + 'processed/Y/binary')
    if not os.path.exists(path + scenario + 'processed/Y/saturation'):
        os.makedirs(path + scenario + 'processed/Y/saturation')
    if not os.path.exists(path + scenario + 'processed/Cb/diff'):
        os.makedirs(path + scenario + 'processed/Cb/diff')
    if not os.path.exists(path + scenario + 'processed/Cb/binary'):
        os.makedirs(path + scenario + 'processed/Cb/binary')
    if not os.path.exists(path + scenario + 'processed/Cb/saturation'):
        os.makedirs(path + scenario + 'processed/Cb/saturation')
    if not os.path.exists(path + scenario + 'processed/Cr/diff'):
        os.makedirs(path + scenario + 'processed/Cr/diff')
    if not os.path.exists(path + scenario + 'processed/Cr/binary'):
        os.makedirs(path + scenario + 'processed/Cr/binary')
    if not os.path.exists(path + scenario + 'processed/Cr/saturation'):
        os.makedirs(path + scenario + 'processed/Cr/saturation')

    # -- post processing --
    if not os.path.exists(path + scenario + 'post_processing/poly_plot'):
        os.makedirs(path + scenario + 'post_processing/poly_plot')
    if not os.path.exists(path + scenario + 'post_processing/histograms'):
        os.makedirs(path + scenario + 'post_processing/histograms')
    if not os.path.exists(path + scenario + 'post_processing/quality_criteria'):
        os.makedirs(path + scenario + 'post_processing/quality_criteria')
