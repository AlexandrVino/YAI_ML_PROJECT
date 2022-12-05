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

    with open(file_name, 'rb') as input_file :
        dataframe = pickle.load(input_file)
    return dataframe['images'].astype('int')
