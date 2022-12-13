from sklearn.cluster import DBSCAN, KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import argparse

from utils.parser import *

def cluster(text, image, choice):
    # preprocessing
    x_c, y_t= centerize(parser(text))
    X = xy_array(x_c, y_t)

    # model choices
    if choice == 'DBSCAN':
        db = DBSCAN(eps=10, min_samples=10).fit(X)
        labels = db.labels_

    elif choice == 'kmeans':
        km = KMeans(n_clusters=2, init='k-means++').fit(X)
        labels = km.labels_

    # draw and show image
    im = plt.imread(image)
    fig = plt.figure(figsize=(10, 10))
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=["cluster-{}".format(x) for x in labels])
    plt.imshow(im, alpha=0.6)
    fig.savefig('{}.png'.format(choice))
    fig.show()

def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    parser.add_argument('--choice', type=str, default='DBSCAN', help='clustering method')
    opt = parser.parse_args()
    return opt

def main(opt):
    cluster(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt(True)
    main(opt)