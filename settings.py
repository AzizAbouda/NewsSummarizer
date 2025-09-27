import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = os.getenv("NEWS_API_URL")