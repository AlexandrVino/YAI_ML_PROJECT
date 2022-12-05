"""
A file that contains functions for uploading files
"""

import pickle

import numpy as np


def load_data(file_name: str) -> np.ndarray:
    """
    :param file_name: path of filename
    :return: read dataset
    """

    with open(file_name, 'rb') as f:
        df = pickle.load(f)
    return df['images'].astype('int')
