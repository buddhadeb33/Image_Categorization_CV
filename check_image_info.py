from PIL import Image
from PIL.ExifTags import TAGS


# This Program extract all information from an image

def extract_exif_info(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is None:
            print("No EXIF data found in the image.")
            return

        print("EXIF Information:")
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            print(f"{tag_name}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    image_path = "/Users/buddha/Desktop/Jaipur_Pushkar/IMG_2661.JPG"
    extract_exif_info(image_path)
