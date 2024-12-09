from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from .config import *
import os
from dotenv import load_dotenv

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': os.getenv("ACCESS_TOKEN_LIFETIME"),  # Время жизни access токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Время жизни refresh токена
    'ALGORITHM': 'HS256',                            # Алгоритм шифрования
    'SIGNING_KEY': os.getenv("SECRET_KEY"),          # Секретный ключ
} 

def create_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }