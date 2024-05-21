import argparse
import shutil
import os
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.vectorstores import Chroma

CHROMA_PATH = "./chroma_db"

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="mistral")  # Ensure this is the correct model
    return embeddings

def query_chroma(query):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )
    
    results = db.similarity_search(query)
    return results

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        print("Database cleared.")
    else:
        print("Database directory does not exist.")

def main():
    parser = argparse.ArgumentParser(description="Query or clear the Chroma database.")
    parser.add_argument('action', type=str, choices=['query', 'clear'], help='Action to perform: query or clear the database.')
    parser.add_argument('--query', type=str, help='The query text to search in the Chroma database.')
    args = parser.parse_args()

    if args.action == 'clear':
        clear_database()
    elif args.action == 'query':
        if not args.query:
            print("Please provide a query using --query.")
            return
        query = args.query
        print(f"Querying for: {query}")
        results = query_chroma(query)
        print("Results:")
        for result in results:
            print(f"Document: {result.metadata['source']}")
            print(f"Page: {result.metadata.get('page')}")
            print(f"Chunk ID: {result.metadata['id']}")
            print(f"Text: {result.page_content}\n")  # Correct attribute is page_content

if __name__ == "__main__":
    main()