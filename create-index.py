# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv 
from pinecone import Pinecone, ServerlessSpec

# loading variables from .env file
load_dotenv() 

# accessing and printing value
print()


pinecore_api_key = os.getenv("PINECORE_API_KEY")

pc = Pinecone(api_key= pinecore_api_key)

# Create Index
index_name = "companies"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

index = pc.Index(index_name)

print(index)
# <pinecone.db_data.index.Index object at 0x10d38d6a0>
