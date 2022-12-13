"""Mine File"""


from utils.load import load_data
from utils.handlers import get_average


arr = load_data('DATA/data_train')
broken_pixels = [{0}, {255}]
for i, image in enumerate(arr):
    mx_x, mx_y, _ = image.shape
    for ii, col in enumerate(image):
        for iii, jjj in enumerate(col):

            if set(jjj) in broken_pixels:
                arr[i, ii, iii] = get_average(ii, iii, mx_x, mx_y, arr[i])
