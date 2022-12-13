import numpy as np


def defective_pixels(images_data):
    for im in range(len(images_data)):
        for row in range(1, len(images_data[im]) - 1):
            for px in range(1, len(images_data[im][row]) - 1):
                if np.array_equal(images_data[im][row][px], np.array([1., 1., 1.])) or np.array_equal(
                        images_data[im][row][px], np.array([0., 0., 0.])):
                    images_data[im][row][px] = np.array([np.median([images_data[im][row - 1][px][0],
                                                                    images_data[im][row - 1][px - 1][0],
                                                                    images_data[im][row - 1][px + 1][0],
                                                                    images_data[im][row + 1][px][0],
                                                                    images_data[im][row + 1][px - 1][0],
                                                                    images_data[im][row + 1][px + 1][0],
                                                                    images_data[im][row][px + 1][0],
                                                                    images_data[im][row][px - 1][0]]),
                                                         np.median([images_data[im][row - 1][px][1],
                                                                    images_data[im][row - 1][px - 1][1],
                                                                    images_data[im][row - 1][px + 1][0],
                                                                    images_data[im][row + 1][px][1],
                                                                    images_data[im][row + 1][px - 1][1],
                                                                    images_data[im][row + 1][px + 1][1],
                                                                    images_data[im][row][px + 1][1],
                                                                    images_data[im][row][px - 1][1]]),
                                                         np.median([images_data[im][row - 1][px][2],
                                                                    images_data[im][row - 1][px - 1][2],
                                                                    images_data[im][row - 1][px + 1][2],
                                                                    images_data[im][row + 1][px][2],
                                                                    images_data[im][row + 1][px - 1][2],
                                                                    images_data[im][row + 1][px + 1][2],
                                                                    images_data[im][row][px + 1][2],
                                                                    images_data[im][row][px - 1][2]])])
    return images_data[0:len(images_data), 1:-1, 1:-1, 0:3]