import os
import shutil
from PIL import Image, ImageEnhance

def adjust_contrast_and_brightness(image_path, contrast_factor, brightness_factor):
    # Open an image file
    with Image.open(image_path) as img:
        # Adjust contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)

        # Adjust brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)

        # Save the modified image back to the same file
        img.save(image_path)

def process_images_in_folder(folder_path, contrast_factor, brightness_factor):
    img_folder = os.path.join(folder_path, 'img')
    
    # Create the img folder if it doesn't exist
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith('.png') and filename not in os.listdir(img_folder):
            image_path = os.path.join(folder_path, filename)
            adjust_contrast_and_brightness(image_path, contrast_factor, brightness_factor)
            print(f'Processed {filename}')
            
            # Move the processed image to the img folder
            shutil.move(image_path, os.path.join(img_folder, filename))

# Get the directory of the current Jupyter Notebook
notebook_path = os.getcwd()

# Example usage
folder_path = notebook_path  # Use the current directory
contrast_factor = 2  # Increase contrast by 100%
brightness_factor = 1  # Increase brightness by 0%

process_images_in_folder(folder_path, contrast_factor, brightness_factor)
