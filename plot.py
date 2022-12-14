import argparse
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns

from utils.parser import *

def plot(text, image, plot, output, model,point_size):
    if model == "deepsort":
        df = parser(text)

    elif model == "bytetrack":
        df = parser_byte(text)

    fig = plt.figure(facecolor="w")
    ax = fig.add_subplot(1, 1, 1, aspect="equal")

    for ID, group in df.groupby('ID'):
        frame = group['frame']
        car_id = group['ID']
        id_max = max(car_id)
        id_min = min(car_id)
        x_min = group['x']
        y_min = group['y']
        w = group['w']
        h = group['h']
        f_max = max(frame)
        f_min = min(frame)
        #print(f_max, f_min, car_id)
            
        # プロットの仕方を指定
        if plot == "scatter" :
            x_c = x_min + w / 2
            y_c = y_min + h
            color = (car_id - id_min) / (id_max - id_min)
            plt.scatter(x_c, y_c, c=frame, cmap='jet',s=point_size)
            
        elif plot == "rectangle" :
            for x, y, w, h, f in zip(x_min, y_min, w, h, frame):
                rect = patch.Rectangle(
                    (x, y),
                    w,
                    h,
                    edgecolor = cm.turbo((f - f_min) / (f_max - f_min)),
                    facecolor = cm.turbo((f - f_min) / (f_max - f_min)),
                    fill=True
                )
                ax.add_patch(rect)
        
        elif plot == "line" :
            x_max = x_min + h
            y_max = y_min + w
            plt.scatter(x_min, y_max, c=frame, cmap="jet")
            plt.scatter(x_max, y_max, c=frame, cmap="jet")
            
        else:
            print("division_by_zero")
    
    # 画像を書き出す
    im = Image.open(image)
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=["cluster-{}".format(x) for x in labels])
    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(output)

def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    parser.add_argument('--plot', type=str, default='scatter', help='set draw style')
    parser.add_argument('--model', type=str, default='deepsort', help='select deepsort or bytetrack')
    parser.add_argument('--point_size', type=float, default='100', help='select point size person=1')
    parser.add_argument('--output', type=str, default='track.png', help='output image name')
    opt = parser.parse_args()
    return opt

def main(opt):
    plot(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt(True)
    main(opt)