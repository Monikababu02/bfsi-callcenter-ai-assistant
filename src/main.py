import json

def load_dataset():
    with open("../dataset/bfsi_dataset.json", "r") as f:
        return json.load(f)

def check_similarity(user_query, dataset):
    for item in dataset:
        if user_query.lower() in item["instruction"].lower():
            return item["output"]
    return None

def rag_response():
    return "This query requires policy-based explanation. Please refer to official documentation."

def main():
    dataset = load_dataset()
    user_query = input("Enter your query: ")

    response = check_similarity(user_query, dataset)

    if response:
        print("Dataset Response:")
        print(response)
    else:
        print("RAG Response:")
        print(rag_response())

if __name__ == "__main__":
    main()

