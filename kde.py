import matplotlib.pyplot as plt
import seaborn as sns

from utils.parser import *

# bboxの中心下部でプロットする

def centerize(text):
    df = parser(text)
    y_list = df.loc[:,'y'].values
    x_list = df.loc[:,'x'].values
    w_list = df.loc[:,'w'].values
    h_list = df.loc[:,'h'].values

    xc_list = x_list + w_list / 2
    yt_list = y_list + h_list
    #print(df)
    return xc_list, yt_list

def kde2d(image, xc_list, yt_list):
    im = plt.imread(image)
    sns.set()
    fig, ax = plt.subplots(figsize = (10,5))
    sns.kdeplot(x=xc_list, y=yt_list, color='C4', fill=True, alpha=0.8, bw_method=0.1)
    plt.imshow(im, alpha=0.7)
    plt.savefig('2Dkde.png')

if __name__ == '__main__':
    xc_list, yt_list = centerize('./texts/Jingubashi.txt')
    kde2d('thumbnails/Jingubashi.png', xc_list, yt_list)