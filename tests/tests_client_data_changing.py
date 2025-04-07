import pytest
import allure
from objects.client import Client
import helpers as h


class TestClientDataChanging:
    @allure.title('Тест на изменение данных с авторизацией')
    @allure.description('Проверяем, что запрос на смену данных вернул статус 200 и в тело запроса есть "success": true и новые параметры соответствуют поданым на вход')
    def test_changing_client_data_return_200_success(self, get_client_data):
        client = get_client_data['client']
        token = get_client_data['register_response'].json()['accessToken']
        new_params = {'email': h.get_random_email(), 'name': h.get_random_name()}
        responce_changed_info = client.changed_info(token, new_params)
        assert responce_changed_info.status_code == 200 and responce_changed_info.json()['success'] and responce_changed_info.json()['user'] == new_params


    @allure.title('Тест на изменение данных без авторизации')
    @allure.description('Проверяем, что запрос на  смену данных вернул статус 401 и в тело запроса есть "success": true')
    def test_changing_client_data_wo_token_return_401_success(self, get_client_data):
        client = get_client_data['client']
        new_params = {'email': h.get_random_email(), 'name': h.get_random_name()}
        responce_changed_info = client.changed_info(new_params=new_params)
        assert responce_changed_info.status_code == 401 and responce_changed_info.json() == {"success": False,
                                                                                             "message": "You should be authorised"}


