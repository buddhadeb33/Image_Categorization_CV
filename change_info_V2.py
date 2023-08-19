import os
import subprocess
from datetime import datetime


def modify_exif_datetime(image_path, new_datetime):
    try:
        # Modify DateTime
        command_datetime = f'exiftool -DateTime="{new_datetime}" -overwrite_original "{image_path}"'
        result_datetime = subprocess.run(command_datetime, shell=True, capture_output=True, text=True, check=True)
        print(result_datetime)

        # Modify DateTimeOriginal
        command_original = f'exiftool -DateTimeOriginal="{new_datetime}" -overwrite_original "{image_path}"'
        result_original = subprocess.run(command_original, shell=True, capture_output=True, text=True, check=True)
        print(result_original)

        # Modify DateTimeDigitized
        command_digitized = f'exiftool -DateTimeDigitized="{new_datetime}" -overwrite_original "{image_path}"'
        result_digitized = subprocess.run(command_digitized, shell=True, capture_output=True, text=True, check=True)
        print(result_digitized)

        print("EXIF data modified successfully.")

        print("DateTime change:")
        print(result_datetime.stdout)

        print("DateTimeOriginal change:")
        print(result_original.stdout)

        print("DateTimeDigitized change:")
        print(result_digitized.stdout)

        # Convert new_datetime to a Unix timestamp
        new_datetime_timestamp = datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S").timestamp()

        try:
            # Change file creation and modification timestamps
            os.utime(image_path, (os.path.getatime(image_path), new_datetime_timestamp))
            print("File timestamps modified successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    except subprocess.CalledProcessError as e:
        print("An error occurred while modifying EXIF data.")
        print("Command output (stderr):")
        print(e.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


def process_images_in_folder(folder_path, new_datetime):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.JPG')):
            image_path = os.path.join(folder_path, filename)
            modify_exif_datetime(image_path, new_datetime)


if __name__ == "__main__":
    # image_path = "/Users/buddha/Desktop/Jaipur_Pushkar/IMG_2661.JPG"
    new_datetime = "2023-08-13 12:10:00"
    # modify_exif_datetime(image_path, new_datetime)
    folder_path = "/Users/buddha/Desktop/Jaipur_Pushkar"
    process_images_in_folder(folder_path, new_datetime)
