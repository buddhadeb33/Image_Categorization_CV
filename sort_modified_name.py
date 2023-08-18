import os
import shutil
from PIL import Image
from datetime import datetime


def sort_images_by_year(source_folder, destination_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(source_folder, file_name)

        # Check if the file is an image
        try:
            with Image.open(file_path) as img:
                # Get the modified date of the image
                modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                year = modified_date.year

                # Create the year folder if it doesn't exist
                year_folder = os.path.join(destination_folder, str(year))
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)

                # Move the image to the year folder
                destination_path = os.path.join(year_folder, file_name)
                shutil.move(file_path, destination_path)

                print(f"Moved '{file_name}' to {year_folder}")
        except (IOError, SyntaxError) as e:
            print(f"Skipped non-image file: {file_name}")


# Example usage:
source_folder = "/Users/buddha/Pictures/Untitled/January/Family/SortedImages"
destination_folder = "/Users/buddha/Pictures/Untitled/January/Family/"

sort_images_by_year(source_folder, destination_folder)
