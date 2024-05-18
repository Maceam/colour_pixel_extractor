from image_colour_extract.colour_extractor import *
import os


# Main execution path change filename to name of .tif file Working directory changed to image_colour_extract/data
filename = "tiff1.tif"
filepath = "image_colour_extract/data/"  # Assuming 'data' folder is directly in the working directory
os.chdir("..")
full_path = os.path.join(os.getcwd(), filepath, filename)
print("Current Working Directory:", os.getcwd())
print("Attempting to open:", full_path)
image = load_image(full_path)
print(image.size, image.mode, image.format)


# Create the array to be saved as a csv
image_array = image_to_array(image)
flat_data = flatten_image_data(image_array)


# Written to change the directory to results and save the file cleanly
print("Current Working Directory:", os.getcwd())
file_result = os.path.join(os.getcwd(), "results/")
os.chdir(file_result)
print("Current Working Directory:", os.getcwd())
print("Attempting to open:", full_path)
save_to_csv(flat_data, 'px_extraction.csv')
