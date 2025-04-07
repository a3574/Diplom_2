import pytest
import allure
from objects.order import Order
from objects.ingredient import Ingredient


class TestOrderCreating:
    @allure.title('Тест на создание заказа с авторизацией и с ингридиентами')
    @allure.description(
        'Передаем на api/orders валидный хэш ингредиентов и токен авторизации. Ожидаем статус 200 и в теле ответа есть "success": true и номер заказа "number"')
    def test_order_creating_w_autorization_return_status_200_success(self, get_client_data):
        token = get_client_data['register_response'].json()['accessToken']
        inredients = Ingredient()
        ingredients_list = []
        ingredients_list.append(inredients.get_list_ingredients()[1]['_id'])
        ingredients_list.append(inredients.get_list_ingredients()[2]['_id'])
        order = Order(ingredients_list)
        order_response = order.create_order_full_answer(authorization=token)
        assert order_response.status_code == 200 and 'number' in order_response.json()['order'] and \
               order_response.json()['success']

    @allure.title('Тест на создание заказа без авторизации')
    @allure.description(
        'Передаем на api/orders валидный хэш ингредиентов без токен авторизации. Ожидаем статус 200 и в теле ответа есть "success": true и номер заказа "number"')
    def test_order_creating_wo_autorization_return_status_200_success(self):
        inredients = Ingredient()
        ingredients_list = []
        ingredients_list.append(inredients.get_list_ingredients()[1]['_id'])
        ingredients_list.append(inredients.get_list_ingredients()[2]['_id'])
        order = Order(ingredients_list)
        order_response = order.create_order_full_answer()
        assert order_response.status_code == 200 and 'number' in order_response.json()['order'] and \
               order_response.json()['success']

    @allure.title('Тест на создание заказа без ингредиентов')
    @allure.description(
        'Передаем на api/orders запрос без хэша ингредиентов и без авторизации. Ожидаем статус 400 и что ответ будет: "success": False, "message": "Ingredient ids must be provided"')
    def test_order_creating_wo_ingredients_return_status_400_success(self):
        order = Order()
        order_response = order.create_order_full_answer()
        assert order_response.status_code == 400 and order_response.json() == {"success": False,
                                                                               "message": "Ingredient ids must be provided"}

    @allure.title('Тест на создание заказа  с неверным хешем ингредиентов')
    @allure.description(
        'Передаем на api/orders запрос с некорреткным хэшем ингредиента и без авторизации. Ожидаем статус 500.')
    def test_order_creating_w_incorrect_ingredients_return_status_500_success(self):
        ingredients_list = []
        ingredients_list.append('Некорректный хэш ингридента, точно.')
        order = Order(ingredients_list)
        order_response = order.create_order_full_answer()
        assert order_response.status_code == 500
