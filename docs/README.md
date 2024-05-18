# Pixel Information Extraction for Large Images

This project was created specifically for extracting data from 
large-resolution images, such as those derived from a Sigma camera 
(.x3f converted to .tif). Considering a single image contains over 
14 million pixels, I needed to write a script for custom extraction, 
as the current solutions are geared towards either batch processing 
or processing smaller images.

## Setting Up the Image
Please format your image as an RGB .tif file, as otherwise, this 
will not function.

## How to Use
- Place the image you wish to extract into the `data` folder within 
  `image_colour_extract`.
- Adjust the filename in `__main__.py` to the name of your .tif file.
- Run `__main__.py`.

## Note
The current saving method overwrites the existing CSV file every 
time it is run. I intend to later add multi-image extraction or 
automatic indexing of the file name if it already exists.

## Excluded files
Due to the size of the generated csv It will not be included as 
a single .tif from an .x3f file was approx 410 mb in size.