import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

from PIL import Image
from utils.parser import *

def scan():
    sns.set()
    sns.set_style('whitegrid', {'grid.kinestyle': '--'})
    sns.set_palette('spring', 8, 0.5)

    im = cv2.imread('thumbnails/nasunobashi.png')
    fig = plt.figure(facecolor="w")
    ax = fig.add_subplot(1, 1, 1, aspect="equal")
    h, w, c = im.shape

    df = parser('./texts/nasunobashi.txt')
    x_c, y_t = centerize(df)
    x_c = x_c.to_numpy()
    y_t = y_t.to_numpy()
    y_t = y_t.astype(int)
    print(min(x_c))

    b = []
    for i in range(h):
        a = []
        for j in y_t:
            if i-1 < y_t[j] <= i+1:
                a.append(x_c[j])
        #print('{} contains {}'.format(i, a))
        b.append(np.average(a))
        
    y_data = [i for i in range(h)]
    
    sns.lineplot(x=b, y=y_data)
    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig('scan1.png')
    
if __name__ == '__main__':
    scan()
