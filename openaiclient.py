import os
import openai
from dotenv import load_dotenv 

# loading variables from .env file
load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")

openaiClient = openai
