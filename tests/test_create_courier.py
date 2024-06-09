import pytest
import allure
import json
import requests
from config import URL
from helpers import get_creation_courier
from data import login_courier, first_name_courier, password_courier
class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_fake_courier_true(self):
        login, first_name = get_creation_courier()
        response = requests.post(f"{URL}api/v1/courier", data={
            "login": login,
            "password": password_courier,
             "firstName": first_name
        })

        assert 201 == response.status_code
        assert '{"ok":true}' == response.text

    @allure.title('Неудачная попытка создания курьера без указания пароля')
    def test_create_fake_courier_without_password_false(self):
        login, first_name = get_creation_courier()
        response = requests.post(f"{URL}api/v1/courier", data={
            "login": login,
             "firstName": first_name
        })

        assert 400 == response.status_code
        assert '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == response.text

    @allure.title('Неудачная попытка создания уже созданного курьера')
    def test_create_created_courier_false(self):

        response = requests.post(f"{URL}api/v1/courier", data={
            "login": login_courier,
            "password": password_courier,
             "firstName": first_name_courier
        })
        response = requests.post(f"{URL}api/v1/courier", data={
            "login": login_courier,
            "password": password_courier,
            "firstName": first_name_courier
        })

        assert 409 == response.status_code
        assert '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}' == response.text
