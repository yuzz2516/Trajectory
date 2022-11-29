import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import argparse

from PIL import Image
from utils.parser import *

def scan(text, image, output):
    # 描画
    sns.set()
    sns.set_style('whitegrid', {'grid.kinestyle': '--'})
    sns.set_palette('spring', 8, 0.5)

    im = cv2.imread(image)
    fig = plt.figure(facecolor="w")
    ax = fig.add_subplot(1, 1, 1, aspect="equal")
    h, w, c = im.shape

    # データ整形
    df = parser(text)
    x_c, y_t = centerize(df)
    x_c, y_t = df2numpy(x_c, y_t)
    print(min(x_c))
    
    thresh = 30
    x_data = []
    for i in range(h):
        a = []
        for j in y_t:
            if i-thresh < y_t[j] <= i+thresh:
                a.append(x_c[j])
        #print('{} contains {}'.format(i, a))
        x_data.append(np.average(a))
        
    y_data = [i for i in range(h)]
    
    sns.lineplot(x=x_data, y=y_data)
    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(output)
    
def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    parser.add_argument('--output', type=str, default='results/scan/Jingubashi_scan.png', help='output image name')
    opt = parser.parse_args()
    return opt
    
if __name__ == '__main__':
    opt = parse_opt(True)
    scan(**vars(opt))
