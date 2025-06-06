import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv 
from pinecone import Pinecone, ServerlessSpec

# loading variables from .env file
load_dotenv() 


pinecore_api_key = os.getenv("PINECORE_API_KEY")

pinecoreClient = Pinecone(api_key= pinecore_api_key)
serverSpec = ServerlessSpec

