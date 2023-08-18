import os
import cv2
import face_recognition

def compute_face_encodings(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    face_locations = face_recognition.face_locations(gray_image, model="cnn")

    # Extract face encodings from the image
    face_encodings = face_recognition.face_encodings(image, face_locations)

    return face_encodings

def detect_identical_faces(input_image_path, target_folder_path, similarity_threshold=0.6):
    # Load the input image
    input_image = cv2.imread(input_image_path)

    # Convert the input image to grayscale
    gray_input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the input image
    input_face_locations = face_recognition.face_locations(gray_input_image, model="cnn")

    # Extract face embeddings from the input image
    input_face_encodings = face_recognition.face_encodings(input_image, input_face_locations)

    # Initialize the count of identical face images
    identical_faces_count = 0

    # Cache face encodings for target images
    target_face_encodings_cache = {}

    # Get the total number of target images
    total_target_images = len(os.listdir(target_folder_path))

    # Iterate through images in the target folder
    for i, filename in enumerate(os.listdir(target_folder_path), 1):
        # Load the image from the target folder
        target_image_path = os.path.join(target_folder_path, filename)

        # Check if face encodings for the target image are already cached
        if target_image_path in target_face_encodings_cache:
            target_face_encodings = target_face_encodings_cache[target_image_path]
        else:
            # Compute face encodings for the target image and cache them
            target_face_encodings = compute_face_encodings(target_image_path)
            target_face_encodings_cache[target_image_path] = target_face_encodings

        # Compare face embeddings between the input image and target image
        for input_encoding in input_face_encodings:
            for target_encoding in target_face_encodings:
                # Calculate the similarity score between the face embeddings
                similarity_score = face_recognition.face_distance([input_encoding], target_encoding)

                # Check if the similarity score is below the threshold
                if similarity_score < similarity_threshold:
                    identical_faces_count += 1

        # Print progress and count of identical face images
        print(f"Processed image {i}/{total_target_images} - {filename}")

    return identical_faces_count

# Example usage
input_image_path = "/Users/buddha/Pictures/Untitled/January/Photos_2022/2020/IMG_20200504_135416.jpg"
target_folder_path = "/Users/buddha/Pictures/Untitled/January/Photos_2022/2020"

print(f"Input image: {input_image_path}")
print(f"Target folder: {target_folder_path}")

identical_faces_count = detect_identical_faces(input_image_path, target_folder_path)
print("Number of identical face images:", identical_faces_count)
