from sklearn.cluster import MeanShift
import numpy as np
import argparse
import seaborn as sns

from utils.parser import *

def mean_shift(text, image):
    x_c, y_t = centerize(parser(text))
    X = xy_array(x_c, y_t)

    ms = MeanShift(bandwidth=200)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print('number of estimated clusters : %d' % n_clusters_)

    import matplotlib.pyplot as plt
    from itertools import cycle

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
        markeredgecolor='k', markersize=14)

    im = plt.imread(image)
    fig = plt.figure(facecolor="w")
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=["cluster-{}".format(x) for x in labels])

    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig('Mean-Shift.png')

    plt.title('Estimated number of clusters: %d' % n_clusters_)

def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt(True)
    mean_shift(**vars(opt))