from PIL import Image, ImageOps
import os
import numpy as np

def has_uniform_border(image_path, border_percentage=0.001, num_samples=100, threshold=5): 
    """
    Checks if an image has a uniform border by sampling points along the border and checking color deviation.
    
    Parameters:
    image_path (str): The path to the image file.
    border_percentage (float): The percentage of the border size to sample for border pixels.
    num_samples (int): The number of points to sample along the border.
    threshold (float): The maximum allowed interquartile range for the border to be considered uniform.
    
    Returns:
    bool: True if the image has a uniform border, False otherwise.
    """
    img = Image.open(image_path)
    width, height = img.size
    border_size = int(min(width, height) * border_percentage)

    def sample_border_points():
        points = []
        # Sample points within the border size
        for x in np.linspace(0, border_size - 1, num_samples // 4, dtype=int):
            points.append(img.getpixel((x, 0)))  # Top border
            points.append(img.getpixel((x, height - 1)))  # Bottom border
        for y in np.linspace(0, border_size - 1, num_samples // 4, dtype=int):
            points.append(img.getpixel((0, y)))  # Left border
            points.append(img.getpixel((width - 1, y)))  # Right border
        return points

    border_colors = np.array(sample_border_points())
    color_iqr = np.subtract(*np.percentile(border_colors, [75, 25], axis=0))

    return np.all(color_iqr < threshold)

def add_black_border(image_path, border_percentage=0.002):
    """
    Adds a black border to the image.

    Parameters:
    image_path (str): The path to the image file.
    border_percentage (float): The percentage of the image's minimum dimension to use as border size.
    """
    img = Image.open(image_path)
    width, height = img.size
    border_size = int(min(width, height) * border_percentage)
    img_with_border = ImageOps.expand(img, border=border_size, fill='black')
    return img_with_border

def process_images(directory='.', overwrite=True):
    processed_count = 0
    total_images = 0
    
    if not overwrite:
        new_folder = os.path.join(directory, "with_borders")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            total_images += 1
            image_path = os.path.join(directory, filename)
            if not has_uniform_border(image_path):
                img_with_border = add_black_border(image_path)
                if overwrite:
                    img_with_border.save(image_path)
                else:
                    img_with_border.save(os.path.join(new_folder, filename))
                processed_count += 1
                print(f"Processed: {filename}")
            else:
                if not overwrite:
                    img = Image.open(image_path)
                    img.save(os.path.join(new_folder, filename))
    
    print(f"Total images considered: {total_images}")
    print(f"Total images processed: {processed_count}")

if __name__ == "__main__":
    directory = input("Enter the directory path (or press Enter to use the current directory): ").strip()
    if not directory:
        directory = '.'
    overwrite = input("Do you want to overwrite the images? (yes/no): ").strip().lower() == 'yes'
    process_images(directory, overwrite)
