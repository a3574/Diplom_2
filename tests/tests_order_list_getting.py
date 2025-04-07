import pytest
import allure
from objects.order import Order
import helpers as h


class TestOrderListGetting:
    @allure.title('Тест на получение списка заказов по токену авторизации')
    @allure.description('Проверяем, что запрос вернул статус 200 и в теле запроса есть "success": true')
    def test_get_order_by_token_w_token_return_200_success(self, get_client_data):
        token = get_client_data['register_response'].json()['accessToken']
        order = Order()
        response_get_order_by_token = order.get_order_by_token(token)
        assert response_get_order_by_token.status_code == 200 and response_get_order_by_token.json()['success']


    @allure.title('Тест на изменение данных без авторизации')
    @allure.description('Проверяем, что запрос на  смену данных вернул статус 401 и в тело запроса есть "success": true')
    def test_changing_client_data_wo_token_return_401_success(self, get_client_data):
        client = get_client_data['client']
        order = Order()
        response_get_order_by_token = order.get_order_by_token()
        assert response_get_order_by_token.status_code == 401 and response_get_order_by_token.json() == {"success": False,
                                                                                             "message": "You should be authorised"}