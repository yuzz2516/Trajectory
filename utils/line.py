from utils.parser import *

trajectory = df2numpy(centerize(parser(text)))
def line(trajectory):
    trajectory.head() 

def parse_opt(opt):
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default='texts/Jingubashi.txt', help='text file tracks with DeepSORT')
    parser.add_argument('--image', type=str, default='thumbnails/Jingubashi.png', help='background image of trajectory plot')
    parser.add_argument('--output', type=str, default='results/scan/Jingubashi_scan.png', help='output image name')
    opt = parser.parse_args()
    return opt
    
if __name__ == '__main__':
    opt = parse_opt(True)
    line(**vars(opt))