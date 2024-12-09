import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env

SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRATION_DELTA = os.getenv("JWT_EXPIRATION_DELTA")
EXCHANGE_API_URL = os.getenv("EXCHANGE_API_URL")
DEBUG = os.getenv("DEBUG") == 'True'