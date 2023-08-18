import os
from PIL import Image
from datetime import datetime
import re

# Path to the main folder containing subfolders and files
main_folder = '/Users/buddha/Pictures/Untitled/January/Photos_2022/Unsorted'
parent_folder = '/Users/buddha/Pictures/Untitled/January/Photos_2022'

# Create the "Unsorted" folder
unsorted_folder = os.path.join(parent_folder, "Unsorted")
if not os.path.exists(unsorted_folder):
    os.mkdir(unsorted_folder)

# Iterate over the root, directories, and files in the main folder
for root, directories, files in os.walk(main_folder):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):

            try:
                # Open the image file
                image = Image.open(file_path)

                # Get the date information from the image metadata
                info = image._getexif()
                print(info)
                if info is None or 36867 not in info:
                    raise ValueError("No EXIF metadata found")

                date_str = info[36867]

                # Parse the date string into a datetime object
                date = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')

            except (AttributeError, KeyError, ValueError) as e:
                # Extract the date from the file name using regular expressions
                pattern = r'(\d{4}-\d{2}-\d{2} \d{2}.\d{2}.\d{2})-\d'
                match = re.search(pattern, filename)
                if match:
                    date_str = match.group(1)
                    date = datetime.strptime(date_str, '%Y-%m-%d %H.%M.%S')
                else:
                    print(f"Skipping {filename} due to missing EXIF metadata and invalid date format")
                    continue

            # Retrieve the modified date from the file system
            modified_timestamp = os.path.getmtime(file_path)
            modified_date = datetime.fromtimestamp(modified_timestamp)
            print("MODIFIED DATE", modified_date)

            # Use the modified date for sorting, if available
            if modified_date > date:
                date = modified_date

            # Extract the year from the datetime object
            year = date.year

            # Create a directory for the year if it doesn't exist within the main folder
            year_directory = os.path.join(parent_folder, str(year))
            if not os.path.exists(year_directory):
                os.mkdir(year_directory)

            # Move the file to the respective year directory
            new_file_path = os.path.join(year_directory, filename)
            os.rename(file_path, new_file_path)

            print(f"Moved {filename} to {year_directory}")
