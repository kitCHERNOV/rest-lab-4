from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .users import UserSerializer
from .security import create_jwt_token  # Импорт функции создания JWT
from .external_api import get_exchange_rates, convert_currency  # Импорт функций для работы с API
from .config import *

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token = create_jwt_token(user)
        return Response(token, status=status.HTTP_200_OK)
    return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exchange_rates(request):
    rates = get_exchange_rates()
    return Response(rates)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert(request):
    from_currency = request.data.get('from_currency')
    to_currency = request.data.get('to_currency')
    amount = request.data.get('amount', 1)

    if not from_currency or not to_currency:
        return Response({"error": "Currency codes are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        result = convert_currency(amount, from_currency, to_currency)
        return Response({"result": result})
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)