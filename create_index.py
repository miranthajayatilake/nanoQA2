import pinecone
import os
import argparse

def init(api_key, environment):
    pinecone.init(api_key=api_key, environment=environment)

def create_index(api_key, environment, INDEX_NAME):
    init(api_key, environment)
    pinecone.create_index(INDEX_NAME, dimension=1536, metric="cosine", pod_type="p1.x1")
    print("New index created")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pinecone_api_key", type=str, required=True)
    parser.add_argument("--pinecone_environment", type=str, required=True)
    parser.add_argument("--index_name", type=str, required=True)
    args = parser.parse_args()

    create_index(args.pinecone_api_key, args.pinecone_environment, args.index_name)