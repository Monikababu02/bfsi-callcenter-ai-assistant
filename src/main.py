import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_dataset():
    with open("../dataset/bfsi_dataset.json", "r") as f:
        return json.load(f)

def find_best_match(user_query, dataset):
    instructions = [item["instruction"] for item in dataset]
    
    query_embedding = model.encode([user_query])
    dataset_embeddings = model.encode(instructions)

    similarities = cosine_similarity(query_embedding, dataset_embeddings)
    best_score = np.max(similarities)
    best_index = np.argmax(similarities)

    if best_score > 0.80:
        return dataset[best_index]["output"], best_score
    return None, best_score

def main():
    dataset = load_dataset()
    user_query = input("Enter your query: ")

    response, score = find_best_match(user_query, dataset)

    print(f"Similarity Score: {score}")

    if response:
        print("\nTier 1: Dataset Response")
        print(response)
    else:
        print("\nTier 2: No strong dataset match. RAG triggered.")
        print("Please refer to official documentation for detailed explanation.")

if __name__ == "__main__":
    main()
