from PIL import Image
import csv
import numpy as np

# Getting image ready for numpy array
def load_image(filepath):
    return Image.open(filepath)

# Getting image ready for numpy array
def image_to_array(image):
    return np.array(image)


# A numpy array is capable of reading the channels and pixel co-ordinates.
# This is faster than doing a nested for loop for the XY co-ordinates.
def flatten_image_data(image_array_extraction):
    rows, cols, channels = image_array_extraction.shape
    index_grid = np.arange(rows * cols).reshape((rows, cols))
    x_grid, y_grid = np.meshgrid(np.arange(cols), np.arange(rows))
    flat_data_extraction = np.column_stack(
        (index_grid.flatten(), x_grid.flatten(), y_grid.flatten(), image_array_extraction.reshape(-1, channels)))
    return flat_data_extraction


# At the moment, this is only for writing a single tif file, this will overwrite the current csv if it exists.
def save_to_csv(data, filename_extract_output):
    with open(filename_extract_output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Pixel_Index', 'X', 'Y', 'R', 'G', 'B'])  # Header
        writer.writerows(data)
