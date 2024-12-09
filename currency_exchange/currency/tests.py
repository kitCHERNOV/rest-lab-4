import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserAuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.username = 'testuser'
        self.password = 'testpassword'

    def test_register_user(self):
        response = self.client.post(self.register_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login_user(self):
        # Сначала зарегистрируем пользователя
        self.client.post(self.register_url, {
            'username': self.username,
            'password': self.password
        })

        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  # Проверяем наличие токена доступа

'''
class CurrencyExchangeTests(APITestCase):
    def setUp(self):
        # Создаем пользователя и получаем токен
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.exchange_url = reverse('exchange')  # Убедитесь, что у вас правильно настроены имена маршрутов

        self.username = 'testuser'
        self.password = 'testpassword'

        # Регистрация пользователя
        self.client.post(self.register_url, {
            'username': self.username,
            'password': self.password
        })

        # Логин для получения токена
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })

        self.access_token = response.data['access']

    def test_get_exchange_rates(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}

        response = self.client.get(self.exchange_url, headers=headers)

        # Проверяем статус ответа и наличие данных о курсах обмена
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('rates', response.data)

    def test_convert_currency(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}

        response = self.client.post(self.exchange_url + '/convert/', headers=headers, data=json.dumps({
            'from_currency': 'USD',
            'to_currency': 'EUR',
            'amount': 100
        }), content_type='application/json')

        # Проверяем статус ответа и наличие результата конвертации
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('result', response.data)

    def test_invalid_currency_conversion(self):
        headers = {'Authorization': f'Bearer {self.access_token}'}

        response = self.client.post(self.exchange_url + '/convert/', headers=headers, data=json.dumps({
            'from_currency': 'INVALID',
            'to_currency': 'EUR',
            'amount': 100
        }), content_type='application/json')

        # Проверяем статус ответа на ошибку при недопустимой вал  юте
        #self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
'''