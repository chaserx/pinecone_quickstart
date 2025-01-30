from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Following the instructions from https://www.pinecone.io/docs/quickstart/
# This script creates an index with the name "nobels"
# It uses the Pinecone API key from the .env file
# It uses the AWS cloud provider and the us-east-1 region

def main():
    load_dotenv()

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    index_name = "nobels" # adjust this to your index name

    pc.create_index(
        name=index_name,
        dimension=2, # adjust this to your model dimensions
        metric="cosine", # adjust this to your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) # adjust this to your cloud provider and region
    )


if __name__ == "__main__":
    main()
