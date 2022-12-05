"""
A file that contains functions for prepare dataset to work
"""
import numpy as np


def get_average(center_x: int, center_y: int, mx_x: int, mx_y: int, img: np.ndarray) -> np.ndarray:
    """
    :param center_x: col index
    :param center_y: row index
    :param mx_x: col len
    :param mx_y: row len
    :param img: current image from dataset
    :return: average of 8 nearest pixels
    """

    count = 0
    summa = np.zeros(3)
    for loc_i in range(center_x - 1, center_x + 2, 1):
        for loc_j in range(center_y - 1, center_y + 2, 1):
            if (loc_i < 0 or loc_j < 0 or loc_i >= mx_x or loc_j >= mx_y or (
                    loc_i, loc_j) == (center_x, center_y)
                ):
                continue
            count += 1
            summa += img[loc_i, loc_j]
    return summa / count
