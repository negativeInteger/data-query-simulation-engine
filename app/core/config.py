from dotenv import load_dotenv
import os

load_dotenv() # Apply environment variables from .env file

SECRET_KEY = os.getenv("SECRET_KEY")

# Raise an error if SECRET_KEY is not set
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables")