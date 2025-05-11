from flask import Flask, request, jsonify
from firebase_config import db
from face_utils import save_uploaded_face, find_match
import cv2
import numpy as np

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    name = request.form.get('name')
    age = request.form.get('age')
    contact = request.form.get('contact')

    print(f"Image reçue : {image.filename}")
    print(f"Nom : {name}, Âge : {age}, Contact : {contact}")

    # Ici, tu peux enregistrer ces infos dans une base de données ou un fichier

    return jsonify({'message': 'Image et informations reçues avec succès'}), 200

@app.route("/compare", methods=["POST"])
def compare():
    file = request.files["image"]
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    img_path = save_uploaded_face(img, folder="temp")

    matches = find_match(img_path)

    if not matches.empty:
        match = matches.iloc[0].to_dict()
        return jsonify({"match_found": True, "match": match})
    else:
        return jsonify({"match_found": False})

if __name__ == "__main__":
    app.run(debug=True)
