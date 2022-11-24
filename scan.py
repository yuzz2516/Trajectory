from sklearn.neighbors import KernelDensity
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

from PIL import Image
from utils.parser import *

def scan():
    sns.set()
    sns.set_style('whitegrid', {'grid.kinestyle': '--'})
    sns.set_palette('spring', 8, 0.5)

    im = cv2.imread('thumbnails/Jingubashi.png')
    fig = plt.figure(facecolor="w")
    ax = fig.add_subplot(1, 1, 1, aspect="equal")
    h, w, c = im.shape

    df = parser('./texts/Jingubashi.txt')
    xc_list, yt_list = centerize(df)
    #x = df['x'].to_numpy()
    #y = df['y'].to_numpy()

    #print(len(x))
    b = []
    for i in range(h):
        a = []
        for j in yt_list:
            if i-30 < yt_list[j] <= i+30:
                a.append(xc_list[j])
        b.append(np.average(a))
        #print('{} contain {}'.format(i, np.average(a)))
    y_data = [i for i in range(h)]
    
    sns.lineplot(x=b, y=y_data)
    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig('scan.png')
    
if __name__ == '__main__':
    scan()
