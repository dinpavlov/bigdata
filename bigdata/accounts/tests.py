from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AuthViewsTests(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.first_name = "test_first_name"
        self.last_name = "test_last_name"
        self.password = "test_password"
        self.data = {
            "username": self.username,
            "first_name": self.first_name,
            "second_name": self.last_name,
            "password": self.password,
        }

    """Тест на получение токенов"""

    def test_get_token_user(self):
        url = reverse("token_obtain_pair")
        user = User.objects.create_user(
            username="test_user",
            first_name="test_first_name",
            last_name="test_last_name",
            password="test_password",
        )
        self.assertEqual(user.is_active, 1, "Active User")
        response = self.client.post(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    """Тест на обновление токена"""

    def test_refresh_token_user(self):
        url_get_token = reverse("token_obtain_pair")
        user = User.objects.create_user(
            username="test_user",
            first_name="test_first_name",
            last_name="test_last_name",
            password="test_password",
        )
        self.assertEqual(user.is_active, 1, "Active User")
        response_get_token = self.client.post(url_get_token, self.data, format="json")
        self.assertEqual(
            response_get_token.status_code,
            status.HTTP_200_OK,
            response_get_token.content,
        )
        refresh_token = response_get_token.data["refresh"]
        url_refresh_token = reverse("token_refresh")
        response_refresh_token = self.client.post(
            url_refresh_token, {"refresh": refresh_token}, format="json"
        )
        self.assertEqual(
            response_refresh_token.status_code,
            status.HTTP_200_OK,
            response_refresh_token.content,
        )

    """Тест на регистрацию"""

    def test_register_user(self):
        url = reverse("register")
        user = {
            "username": "test_1",
            "first_name": "test_first_name_1",
            "last_name": "test_last_name_1",
            "password": "test_password_1",
        }
        response = self.client.post(url, data=user, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
