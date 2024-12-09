Currency Exchange API

1. Запустите сервер.
Убедитесь, что вы находитесь в терминале в директории проекта ...\currency_exchange> и выполните команду:
python manage.py runserver

2. Регистрация пользователя.
На странице [http://127.0.0.1:8000/auth/register/] зарегистрируйте пользователя, отправив JSON запрос:
{
    "username": "user1",
    "password": "1"
}

3. Получение токена.
На странице [http://127.0.0.1:8000/auth/login/] получите токен, отправив JSON запрос:
{
    "username": "user1",
    "password": "1"
}

4. Получение списка всех валют.
В терминале (например, в PyCharm), убедитесь, что вы находитесь в директории ...\currency_exchange> и выполните следующий запрос (замените токен на ваш):
$headers = @{
    "Authorization" = "Bearer your_access_token_here"
}
$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/currency/exchange/" -Method GET -Headers $headers
# Выводим ответ
$response.Content

5. Конвертация валюты.
Для перевода из одной валюты в другую выполните следующий запрос (замените токен на ваш и укажите нужные валюты и их количество):
$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Bearer your_access_token_here"
}
$body = @{
    from_currency = "USD"
    to_currency = "EUR"
    amount = 1
} | ConvertTo-Json
Invoke-WebRequest -Uri http://127.0.0.1:8000/currency/convert/ -Method POST -Headers $headers -Body $body



Используемые технологии
Django: веб-фреймворк для создания приложения.
Django REST Framework: для создания API.
JWT (JSON Web Tokens): для аутентификации пользователей.
Requests: для работы с внешними API.
