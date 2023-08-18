import os
import shutil

# Source directory containing subdirectories and images
source_directory = '/Users/buddha/Pictures/Untitled/January/Family/Unknown'

# Destination directory to save all images
destination_directory = '/Users/buddha/Pictures/Untitled/January/Family/SortedImages'

# Iterate over the root, directories, and files in the source directory
for root, directories, files in os.walk(source_directory):
    for filename in files:
        import os
        import shutil

        # Source directory containing subdirectories and images
        source_directory = '/Users/buddha/Pictures/Untitled/January/Family/Unknown'

        # Destination directory to save all images
        destination_directory = '/Users/buddha/Pictures/Untitled/January/Family/SortedImages'

        # Iterate over the root, directories, and files in the source directory
        for root, directories, files in os.walk(source_directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Check if the file is an image
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Create the destination path by joining the destination directory with the filename
                    destination_path = os.path.join(destination_directory, filename)

                    # Move the image file to the destination directory
                    shutil.move(file_path, destination_path)

                    print(f"Moved {filename} to {destination_path}")
        file_path = os.path.join(root, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Get the relative path from the source directory to the current directory
            relative_path = os.path.relpath(root, source_directory)

            # Create the corresponding subdirectories in the destination directory
            destination_subdirectory = os.path.join(destination_directory, relative_path)
            os.makedirs(destination_subdirectory, exist_ok=True)

            # Create the destination path by joining the destination subdirectory with the filename
            destination_path = os.path.join(destination_subdirectory, filename)

            # Copy the image file to the destination directory
            shutil.copy(file_path, destination_path)

            print(f"Copied {filename} to {destination_path}")
