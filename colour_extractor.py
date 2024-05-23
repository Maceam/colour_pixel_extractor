from PIL import Image
import csv
import numpy as np
import os


def path_setup():
    filepath = "image_colour_extract/data/"  # Assuming 'data' folder is directly in the working directory
    filename = input('Enter the name of the image and file type: ')
    os.chdir("..")
    full_path = os.path.join(os.getcwd(), filepath, filename)
    print("Current Working Directory:", os.getcwd())
    print("Attempting to open:", full_path)
    while not os.path.exists(os.path.join(os.getcwd(), filepath, filename)):
        filename = input('Please try again, enter the name of the image and file type: ')
        print(filename)
        print("Current Working Directory:", os.getcwd())
        print("Attempting to open:", full_path)
        print(os.path.join(os.getcwd(), filepath, filename))
    full_path = os.path.join(os.getcwd(), filepath, filename)
    return full_path


def image_setup(full_path):
    image = load_image(full_path)
    print(image.size, image.mode, image.format)
    return image


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
# We need to add an if statement incase there is an alpha chanel
def save_to_csv(data, image, filename_extract_output):
    with open(filename_extract_output, 'w', newline='') as file:
        colour_mode = str(image.mode)
        if colour_mode == 'RGBA' or colour_mode == 'RGBX':
            writer = csv.writer(file)
            writer.writerow(['Pixel_Index', 'X', 'Y', 'R', 'G', 'B', 'A'])  # Header
            writer.writerows(data)
        else:
            writer = csv.writer(file)
            writer.writerow(['Pixel_Index', 'X', 'Y', 'R', 'G', 'B'])  # Header
            writer.writerows(data)
