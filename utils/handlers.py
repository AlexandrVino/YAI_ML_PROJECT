"""
A file that contains functions for prepare dataset to work
"""
import numpy as np


def get_average(x: int, y: int, mx_x: int, mx_y: int, img: np.ndarray) -> np.ndarray:
    """
    :param x: col index
    :param y: row index
    :param mx_x: col len
    :param mx_y: row len
    :param img: current image from dataset
    :return: average of 8 nearest pixels
    """

    c = 0
    sm = np.zeros(3)
    for k in range(x - 1, x + 2, 1):
        for kk in range(y - 1, y + 2, 1):
            if k < 0 or kk < 0 or k >= mx_x or kk >= mx_y or (k, kk) == (x, y):
                continue
            c += 1
            sm += img[k, kk]
    return sm / c
