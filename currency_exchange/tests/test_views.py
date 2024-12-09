# Файл: tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserTests(APITestCase):

    def test_register(self):
        url = reverse('register')  # Убедитесь, что у вас есть соответствующий путь в urls.py
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)