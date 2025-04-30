from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from ultralytics import YOLO
import os

app = Flask(__name__)
CORS(app)  


model = YOLO("best_umur.pt")

@app.route('/deteksi', methods=['POST'])
def deteksi():
    
    file = request.files['foto']
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

    
    img_np = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

    
    if frame is None:
        return jsonify({'error': 'Invalid image'}), 400

    
    results = model(frame)

    umur_padi = "Tidak terdeteksi"
    confidence = 0

    
    for r in results:
        for box, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
            label = model.names[int(cls)]
            print(f"Label yang terdeteksi: {label}, Confidence: {conf.item() * 100}%")
            umur_padi = int(label.split("_")[1])
            confidence = round(conf.item() * 100, 2)
            break  

    return jsonify({'umur_padi': umur_padi, 'confidence': confidence})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
