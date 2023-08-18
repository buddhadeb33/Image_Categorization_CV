import os
import cv2
import face_recognition

def detect_identical_faces(input_image_path, target_folder_path, similarity_threshold=0.6):
    # Load the input image
    input_image = cv2.imread(input_image_path)

    # Convert the input image to grayscale
    gray_input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the input image
    input_face_locations = face_recognition.face_locations(gray_input_image)

    # Extract face embeddings from the input image
    input_face_encodings = face_recognition.face_encodings(input_image, input_face_locations)

    # Initialize the count of identical face images
    identical_faces_count = 0

    # Iterate through images in the target folder
    for filename in os.listdir(target_folder_path):
        # Load the image from the target folder
        target_image_path = os.path.join(target_folder_path, filename)
        target_image = cv2.imread(target_image_path)

        # Convert the target image to grayscale
        gray_target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the target image
        target_face_locations = face_recognition.face_locations(gray_target_image)

        # Extract face embeddings from the target image
        target_face_encodings = face_recognition.face_encodings(target_image, target_face_locations)

        # Compare face embeddings between the input image and target image
        for input_encoding in input_face_encodings:
            for target_encoding in target_face_encodings:
                # Calculate the similarity score between the face embeddings
                similarity_score = face_recognition.face_distance([input_encoding], target_encoding)

                # Check if the similarity score is below the threshold
                if similarity_score < similarity_threshold:
                    identical_faces_count += 1

    return identical_faces_count

# Example usage
input_image_path = "/Users/buddha/Pictures/Untitled/January/Photos_2022/2020/IMG_20200504_135416.jpg"
target_folder_path = "/Users/buddha/Pictures/Untitled/January/Photos_2022/2020"

identical_faces_count = detect_identical_faces(input_image_path, target_folder_path)
print("Number of identical face images:", identical_faces_count)
