import requests
import allure
from urls import INGREDIENTS

class Ingredient:
    @allure.step('Получение ответа от API ингредиентов')
    def get_ingredients(self):
        responce_get_ingredients = requests.get(url=INGREDIENTS)
        return responce_get_ingredients
    @allure.step('Получение списка ингредиентов')
    def get_list_ingredients(self):
        list_ingredients = self.get_ingredients().json()['data']
        return list_ingredients
