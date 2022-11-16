import argparse
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from PIL import Image


def plot(text, image, plot):
    # データの整形
    f = pd.read_csv(text, sep=' ')
    df = pd.DataFrame(f)
    df.columns = ['frame', 'ID', 'x', 'y', 'w', 'h', 'n1', 'n2', 'n3', 'n4', 'n5']

    df = df.drop(columns=["n1", "n2", "n3", "n4", "n5"])
    #print(df)
    sum_frame = len(df)

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
            x_c = x_min + h / 2
            y_c = y_min + w
            color = (car_id - id_min) / (id_max - id_min)
            plt.scatter(x_c, y_c, c=frame, cmap='jet')
            
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
    plt.imshow(im, alpha=0.6)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig('track.png')

def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    parser.add_argument('--plot', type=str, default='scatter', help='set draw style')
    opt = parser.parse_args()
    return opt

def main(opt):
    plot(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt(True)
    main(opt)