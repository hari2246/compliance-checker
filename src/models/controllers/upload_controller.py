from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to save uploaded PDFs
UPLOAD_FOLDER = 'data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return jsonify({"message": "File uploaded successfully", "file_path": filepath}), 200
    else:
        return jsonify({"error": "Only PDF files are allowed"}), 400

if __name__ == "__main__":
    app.run(debug=True)
