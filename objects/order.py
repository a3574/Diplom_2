import requests
import allure
from urls import ORDER_LIST, ORDER


class Order:
    def __init__(self, ingredients=None):
        self.ingredients = ingredients

    @allure.step('Получение ответа от API списка заказов')
    def get_orders_full_answer(self):
        responce_get_orders = requests.get(url=ORDER_LIST)
        return responce_get_orders

    @allure.step('Получение списка заказов из ответа API списка заказов')
    def get_orders_only_list_order(self):
        list_orders = self.get_orders_full_answer().json()['orders']
        return list_orders

    @allure.step('Получение ответа от API создания заказа')
    def create_order_full_answer(self, authorization=None, params=None):
        headers = {}
        if self.ingredients:
            params = {'ingredients': self.ingredients}
        if authorization:
            headers['authorization'] = authorization
            responce_create_order = requests.post(url=ORDER, headers=headers, data=params)
        else:
            responce_create_order = requests.post(url=ORDER, data=params)
        return responce_create_order

    @allure.step('Получение инфо по заказу из ответа API создания заказа')
    def create_order_only_order(self):
        order = self.create_order_full_answer().json()['order']
        return order

    @allure.step('Получить заказы конкретного пользователя')
    def get_order_by_token(self, token=None):
        headers = {}
        if token:
            headers['authorization'] = token
            responce_get_order_by_token = requests.get(url=ORDER, headers=headers)
        else:
            responce_get_order_by_token = requests.get(url=ORDER)
        return responce_get_order_by_token
