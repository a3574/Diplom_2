import requests
import allure
from urls import CLIENT_REGISTER, CLIENT_LOGIN, CLIENT_RESET_PASSWORD, CLIENT_NEW_PASSWORD, CLIENT_LOGOUT, \
    CLIENT_REFRESH_TOKEN, CLIENT_INFO


class Client:
    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password

    @allure.step('Создание пользователя через post запрос.')
    def register(self):
        params = {}
        if self.email:
            params['email'] = self.email
        if self.name:
            params['name'] = self.name
        if self.password:
            params['password'] = self.password
        responce_register = requests.post(url=CLIENT_REGISTER, data=params)
        return responce_register

    @allure.step('Логин пользователя через post запрос')
    def login(self):
        params = {}
        if self.email:
            params['email'] = self.email
        if self.password:
            params['password'] = self.password
        responce_login = requests.post(url=CLIENT_LOGIN, data=params)
        return responce_login

    @allure.step('Получение Bearer токена после логина')
    def get_access_token(self):
        access_token = self.login().json()['accessToken']
        return access_token

    @allure.step('Выход пользователя через post запрос')
    def logout(self, token=None):
        params = {}
        if token:
            params['token'] = token
        responce_logout = requests.post(url=CLIENT_LOGOUT, data=params)
        return responce_logout

    @allure.step('Обновление токена пользователя через post запрос')
    def refresh_token(self):
        params = {}
        if self.email:
            params['email'] = self.email
        if self.password:
            params['password'] = self.password
        responce_refresh_token = requests.post(url=CLIENT_REFRESH_TOKEN, data=params)
        return responce_refresh_token

    @allure.step('Получение и обновление информации о пользователе через get запрос')
    def changed_info(self, authorization=None, new_params=None):
        params = new_params
        headers = {}
        if authorization:
            headers['authorization'] = authorization
            responce_changed_info = requests.patch(url=CLIENT_INFO, headers=headers, data=params)
        else:
            responce_changed_info = requests.patch(url=CLIENT_INFO, data=params)
        return responce_changed_info

    @allure.step('Удаление информации о пользователе через delete запрос')
    def delete_info(self, authorization=None):
        headers = {}
        if authorization:
            headers['authorization'] = authorization
        responce_delete_info = requests.delete(url=CLIENT_INFO, headers=headers)
        return responce_delete_info

    @allure.step('Сброс пароля через post запрос')
    def reset_password(self):
        params = {}
        if self.email:
            params['email'] = self.email
        responce_reset_password = requests.post(url=CLIENT_RESET_PASSWORD, data=params)
        return responce_reset_password

    @allure.step('Сброс пароля через post запрос')
    def set_new_password(self):
        params = {}
        if self.email:
            params['email'] = self.email
        responce_set_new_password = requests.post(url=CLIENT_NEW_PASSWORD, data=params)
        return responce_set_new_password
