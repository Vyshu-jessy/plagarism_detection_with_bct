from flask import Flask, render_template, request
import os
from utils import load_documents, preprocess, compute_similarity, detect_ai_text, hash_function
from blockchain import add_record

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['document']
        if file and file.filename.endswith('.txt'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            input_text = preprocess(load_documents(filepath))
            source_files = ['data/source1.txt', 'data/source2.txt']
            sources = [preprocess(load_documents(doc)) for doc in source_files]

            # Plagiarism check
            plagiarized, similarity_score = compute_similarity(input_text, sources)

            # AI detection check
            ai_detected, ai_score = detect_ai_text(input_text)

            # Blockchain record (hashing the input text)
            doc_hash = hash_function(input_text)
            tx_hash = add_record(doc_hash, plagiarized)

            result = {
                "plagiarized": plagiarized,
                "similarity_score": round(similarity_score, 2),
                "ai_detected": ai_detected,
                "ai_score": round(ai_score, 2),
                "tx_hash": tx_hash
            }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
