from utils import load_documents, preprocess, compute_similarity, detect_ai_text

# Define file paths
input_doc_path = 'uploads/input.txt'
source_doc_paths = ['data/source1.txt', 'data/source2.txt']

# Load and preprocess documents
input_text = preprocess(load_documents(input_doc_path))
source_texts = [preprocess(load_documents(path)) for path in source_doc_paths]

# --- Plagiarism Detection ---
plagiarized, similarity_score = compute_similarity(input_text, source_texts)
print("----- Plagiarism Check -----")
print(f"Plagiarism Detected: {plagiarized}")
print(f"Max Similarity Score: {similarity_score:.2f}")

# --- AI-Generated Content Detection ---
ai_detected, ai_score = detect_ai_text(input_text)
print("\n----- AI Content Check -----")
print(f"AI-Generated Text: {ai_detected}")
print(f"AI-Likeness Score: {ai_score:.2f}")
