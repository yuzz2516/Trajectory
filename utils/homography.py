import pandas as pd
import numpy as np
import cv2

from utils.parser import *

def homography_trans(
        p_original:list,
        p_trans:list
    )->np.ndarray:
    """_summary_

    Args:
        p_original (list): _description_
        p_trans (list): _description_

    Returns:
        np.ndarray: _description_
    """

    # 変換前後の対応点を設定
    p_original = np.float32(p_original)
    p_trans = np.float32(p_trans)

    # 変換マトリクスと射影変換yo
    M = cv2.getPerspectiveTransform(p_original, p_trans)

    return M


def point_to_list(x1,y1,x2,y2,x3,y3,x4,y4):
    p_original_list = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]

    return p_original_list

if __name__ == '__main__':
    homography_trans()

