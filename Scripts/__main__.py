from image_colour_extract.colour_extractor import *
import os

# These help to create the working directory and select the correct image
full_path = path_setup()
img_manipulate = image_setup(full_path)

# Create the array to be saved as a csv, we need to manipulate ir first before we can flatten it
image_array = image_to_array(img_manipulate)
flat_data = flatten_image_data(image_array)

# Written to change the directory to results and save the file cleanly
# Warning, Currently this will overwrite any csv with the same name
file_result = os.path.join(os.getcwd(), "results/")
os.chdir(file_result)
csv_name = input("Name of csv output, do not add filetype: ") + '.csv'
print('saving ' + csv_name)
save_to_csv(flat_data, img_manipulate, csv_name)
