import matplotlib.pyplot as plt
import seaborn as sns

from utils.parser import *

# bboxの中心下部でプロットする

def kde2d(image, xc_list, yt_list):
    im = plt.imread(image)
    sns.set()
    fig, ax = plt.subplots(figsize = (10,5))
    sns.kdeplot(x=xc_list, y=yt_list, color='C4', fill=True, alpha=0.8, bw_method=0.1)
    plt.imshow(im, alpha=0.7)
    plt.savefig('2Dkde.png')

if __name__ == '__main__':
    x_c, y_t = centerize(parser('./texts/kanetsu.txt'))
    kde2d('thumbnails/kanetsu.png', x_c, y_t)