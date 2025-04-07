import pytest
import allure
from objects.client import Client
import helpers as h


class TestClientRegistering:
    @allure.title('Тест создание уникального пользователя')
    @allure.description('Проверяем, что запрос регистрации вернул статус 200 и в тело запроса есть "success": true')
    def test_registered_client_return_200_success(self, get_client_data):
        assert get_client_data['register_response'].status_code == 200 and get_client_data['register_response'].json()['success']

    @allure.title('Тест на создание пользователя, который уже существует')
    @allure.description(
        'Проверяем, что запрос на регистрацию вернул статус 403 и в тело запроса содержит фразу: "success": False, "message": "User already exists"')
    def test_registered_client_twice_return_403_success(self, get_client_data):
        email = get_client_data['register_response'].json()['user']['email']
        name = get_client_data['register_response'].json()['user']['name']
        password = h.get_random_password()
        new_client = Client(email=email, name=name, password=password)
        new_client_responce = new_client.register()
        assert new_client_responce.status_code == 403 and new_client_responce.json() == {"success": False,
                                                                                         "message": "User already exists"}

    @allure.title('Тест на создание пользователя, без одного из обязательных полей')
    @allure.description(
        'Проверяем, что запрос на регистрацию вернул статус 403 и в тело запроса содержит фразу: "success": False, "message": "Email, password and name are required fields"')
    def test_registered_client_without_required_feild_return_403_success(self):
        email = h.get_random_email()
        name = h.get_random_name()
        password = h.get_random_password()
        client_without_name = Client(email=email, password=password)
        client_without_name_responce = client_without_name.register()
        client_without_email = Client(name=name, password=password)
        client_without_email_responce = client_without_name.register()
        client_without_password = Client(email=email, name=name)
        client_without_password_responce = client_without_name.register()
        assert client_without_name_responce.status_code == 403 and client_without_name_responce.json() == {
            "success": False,
            "message": "Email, password and name are required fields"} and client_without_email_responce.status_code == 403 and client_without_email_responce.json() == {
                   "success": False,
                   "message": "Email, password and name are required fields"} and client_without_password_responce.status_code == 403 and client_without_password_responce.json() == {
                   "success": False, "message": "Email, password and name are required fields"}
