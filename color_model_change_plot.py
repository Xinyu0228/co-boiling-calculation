
from matplotlib import pyplot as plt
import matplotlib

def color_model_change_plot(img_bin, V_BAL):
    print('Plotting an overview plot for binary conversion...')

    list_indices = [[11, 12, 13, 14, 15, 16, 17, 18, 19, 10],  # ots
                    [21, 22, 23, 24, 25, 26, 27, 28, 29, 20],  # tri
                    [35, 40, 45, 50, 55, 60, 65, 70, 75, 30],  # m3
                    [36, 41, 46, 51, 56, 61, 66, 71, 76, 31],  # m5
                    [37, 42, 47, 52, 57, 62, 67, 72, 77, 32],  # m7
                    [38, 43, 48, 53, 58, 63, 68, 73, 78, 33],  # m9
                    [39, 44, 49, 54, 59, 64, 69, 74, 79, 34],  # me11
                    [85, 90, 95, 100, 105, 110, 115, 120, 125, 80],  # g3
                    [86, 91, 96, 101, 106, 111, 116, 121, 126, 81],  # g5
                    [87, 92, 97, 102, 107, 112, 117, 122, 127, 82],  # g7
                    [88, 93, 98, 103, 108, 113, 118, 123, 128, 83],  # g9
                    [89, 94, 99, 104, 109, 114, 119, 124, 129, 84],  # g11
                    [131, 132, 133, 134, 135, 136, 137, 138, 139, 130]]  # min
    i = 0
    while i < len(list_indices):
        print("list_indices=",len(list_indices))
        fig = plt.figure(figsize=(6, 10))
        matplotlib.rcParams.update({'font.size': 12})
        fig.subplots_adjust(hspace=0.35, wspace=0.05, left=0.002, right=0.9998, bottom=0.03, top=0.97)
        for b in range(len(list_indices[i])):
            print("i=",i)
            print("b=",b)
            sp = fig.add_subplot(4, 3, (b + 1))
            print("img_bin.qc is",img_bin.qc)
            if img_bin.qc[list_indices[i][b]-10] != 1.0:
                sp.imshow(img_bin.data[list_indices[i][b]], cmap='gray')
            sp.set_title(img_bin.colour_space[list_indices[0][b]-10].replace('_absdiff', ''))
            sp.axis('off')
            sp.text(0.5, -0.1, s='$QC_{diff}$ (-): ' + str(round(img_bin.qc[list_indices[i][b]-10] / V_BAL, 4)),
                    size=12, ha="center", transform=sp.transAxes)
            print(img_bin.qc[list_indices[i][b]-10] / V_BAL)
        fig.savefig(img_bin.path + img_bin.scenario + 'post_processing/color_model_change_plot/' +
                    img_bin.colour_space[list_indices[i][0]] + '.png', dpi=300)
        i += 1

        plt.close()

