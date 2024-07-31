# Image Border Adder

This project provides a Python script to add black borders to images in a specified directory. The script checks if the images already have a uniform black border and, if not, adds one. The user can choose whether to overwrite the original images or save all images (both processed and unprocessed) in a new folder.

## Requirements

- Python 3.x
- PIL (Pillow)
- numpy
- os

## Installation

To install the required packages, run:

```bash
pip install Pillow numpy
```

## Usage
Run the script using the following command:

```python
python add_border.py
```

# Parameters

- `image_path (str)`: The path to the image file.
- `border_percentage (float)`: The percentage of the image's minimum dimension to use as border size. Default is 0.2%.
- `num_samples (int)`: The number of points to sample along the border. Default is 100.
- `threshold (float)`: The maximum allowed standard deviation for the border to be considered uniform. Default is 5.

# Functions

## `has_uniform_border(image_path, border_percentage=0.001, num_samples=100, threshold=5)`

Checks if an image has a uniform border by sampling points along the border and checking color deviation.

**Parameters:**
- `image_path (str)`: The path to the image file.
- `border_percentage (float)`: The percentage of the border size to sample for border pixels. Default is 0.1%.
- `num_samples (int)`: The number of points to sample along the border. Default is 100.
- `threshold (float)`: The maximum allowed standard deviation for the border to be considered uniform. Default is 5.

**Returns:**
- `bool`: True if the image has a uniform border, False otherwise.

## `add_black_border(image_path, border_percentage=0.002)`

Adds a black border to the image.

**Parameters:**
- `image_path (str)`: The path to the image file.
- `border_percentage (float)`: The percentage of the image's minimum dimension to use as border size. Default is 0.2%.

## `process_images(directory='.', overwrite=True)`

Processes all images in the specified directory, adding black borders where necessary. The user can choose to overwrite the original images or save all images in a new folder.

**Parameters:**
- `directory (str)`: The directory path containing the images. Default is the current directory.
- `overwrite (bool)`: Whether to overwrite the original images. Default is True.

# Notes

- The script processes only images with the following extensions: `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif`.
- The script prints the total number of images considered and the number of images processed.

# License

This project is licensed under the MIT License. See the LICENSE file for details.
