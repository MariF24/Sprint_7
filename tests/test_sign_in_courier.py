import pytest
import allure
import json
import requests
from config import URL
from data import login_courier, password_courier, login_courier_null, password_courier_null

class TestSignInCourier:

    @allure.title('Успешная авторизация курьера')
    def test_sign_in_courier_true(self):
        response = requests.post(f"{URL}api/v1/courier/login", data={
            "login": login_courier,
            "password": password_courier
        })

        assert 200 == response.status_code
        assert '{"id":330171}' == response.text

    @allure.title('Неудачная попытка авторизации курьера без указания пароля')
    def test_sign_in_courier_without_password_false(self):
        response = requests.post(f"{URL}api/v1/courier/login", data={
            "login": login_courier,
            "password": ""
        })

        assert 400 == response.status_code
        assert '{"code":400,"message":"Недостаточно данных для входа"}' == response.text

    @allure.title('Неудачная попытка авторизации еще не созданного курьера')
    def test_sign_in_null_courier(self):
        response = requests.post(f"{URL}api/v1/courier/login", data={
            "login": login_courier_null,
            "password": password_courier_null
        })

        assert 404 == response.status_code
        assert '{"code":404,"message":"Учетная запись не найдена"}' == response.text

