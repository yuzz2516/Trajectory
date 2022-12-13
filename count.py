import argparse
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from PIL import Image

from utils.parser import *


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



def count(text, image, model, output,range):
    if model == "deepsort":
        df = parser(text)

    elif model == "bytetrack":
        df = parser_byte(text)

    range = 0 

    



def main(opt):
    count(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt(True)
    main(opt)

count()
