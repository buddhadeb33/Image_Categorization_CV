from PIL import Image
import piexif

def modify_exif_datetime(image_path, new_datetime):
    try:
        image = Image.open(image_path)
        exif_dict = piexif.load(image.info.get("exif"))

        if exif_dict:
            new_exif = exif_dict.copy()

            new_exif["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_datetime
            print("Modified DateTimeOriginal:", new_exif["Exif"][piexif.ExifIFD.DateTimeOriginal])
            new_exif["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_datetime
            print("Modified DateTimeDigitized:", new_exif["Exif"][piexif.ExifIFD.DateTimeDigitized])

            exif_bytes = piexif.dump(new_exif)
            image.save("modified_image.jpg", exif=exif_bytes)

            print("EXIF data modified and saved successfully.")
        else:
            print("No EXIF data found in the image.")
    except FileNotFoundError:
        print("File not found.")
    except piexif._exceptions.InvalidImageDataError:
        print("Invalid EXIF data found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    image_path = "/Users/buddha/Desktop/Jaipur_Pushkar/IMG_2661.JPG"
    new_datetime = "2023:08:13 12:10:00"
    modify_exif_datetime(image_path, new_datetime)
