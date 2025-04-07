import pytest
import allure
from objects.client import Client
import helpers as h


class TestClientLogining:
    @allure.title('Тест логин под существующим пользователем')
    @allure.description('Проверяем, что запрос на логин вернул статус 200 и в тело запроса есть "success": true')
    def test_logining_client_return_200_success(self, get_client_data):
        response_login = get_client_data['client'].login()
        assert response_login.status_code == 200 and response_login.json()['success']

    @allure.title('Тест логин с неверным логином и паролем')
    @allure.description(
        'Проверяем, что запрос на логин вернул статус 401 и в тело запроса содержит фразу: "success": False, "message": "email or password are incorrect"')
    def test_registered_client_twice_return_403_success(self):
        name = h.get_random_name()
        email = h.get_random_password()
        password = h.get_random_password()
        client = Client(email=email, name=name, password=password)
        client_login_responce = client.login()
        assert client_login_responce.status_code == 401 and client_login_responce.json() == {"success": False,
                                                                                             "message": "email or password are incorrect"}
