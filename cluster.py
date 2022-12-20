from sklearn.cluster import DBSCAN, KMeans, OPTICS, MeanShift
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import math
import argparse

from utils.parser import *

def preprocess(text, image, choice):
    # preprocessing
    df = parser(text)

    track_ids = []
    vectors = []
    gp = df.groupby('ID')
    for idx, df_g in gp:
        x = df_g['x'].tolist()
        y = df_g['y'].tolist()
        f = df_g['frame'].tolist()
        for i in range(len(x)-1):
            arr = np.hstack((idx, f[i], x[i], y[i]))
            track_ids.append(arr)
            vector_x = x[i+1] - x[i]
            vector_y = y[i+1] - y[i]

            #print('ID:{} (x={}, y={})'.format(idx, vector_x, vector_y))
            # ベクトル化
            u = (0, 1)
            v = (vector_x, vector_y)
            inner = np.inner(u, v)
            norm = LA.norm(u) * LA.norm(v)
            if inner and norm != 0:
                c = inner / norm
            a = np.rad2deg(np.arccos(np.clip(c, -1., 1.)))
            
            vectors.append([x[i], y[i], a, idx])
    return text, image, choice, vectors

def cluster(text, image, choice, vectors):
    X = np.array(vectors)
    #print(X)

    # model choices
    if choice == 'DBSCAN':
        db = DBSCAN(eps=10, min_samples=10).fit(X)
        labels = db.labels_

    elif choice == 'kmeans':
        km = KMeans(n_clusters=2, init='k-means++').fit(X)
        labels = km.labels_

    elif choice == 'OPTICS':
        op = OPTICS(min_samples=50, xi=.05, min_cluster_size=.05)
        labels = op.fit(X)

        labels = cluster_optics_dbscan(reachability=op.reachability_,
                                   core_distances=op.core_distances_,
                                   ordering=op.ordering_, eps=0.5)

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

if __name__ == "__main__":
    opt = parse_opt(True)
    text, image, choice, vectors = preprocess(**vars(opt))
    cluster(text, image, choice, vectors)