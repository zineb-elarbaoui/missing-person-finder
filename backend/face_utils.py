from deepface import DeepFace
import cv2
import os
import uuid

def save_uploaded_face(image, folder="faces_db"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.jpg"
    path = os.path.join(folder, filename)
    cv2.imwrite(path, image)
    return path

def find_match(img_path, db_path="faces_db"):
    result = DeepFace.find(img_path, db_path=db_path, enforce_detection=False)
    return result[0] if result else []
