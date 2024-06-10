import pytest
import allure
import json
import requests
from config import URL

class TestListOrder:

    @allure.title('Проверка получения списка заказов без указания id курьера')
    def test_get_list_order_without_id_courier_true(self):
        response = requests.get(f"{URL}api/v1/orders")

        assert 200 == response.status_code
        assert '{"orders":[' in response.text


    @allure.title('Проверка получения списка заказов c несуществующим id курьера')
    def test_get_list_order_null_id_courier(self):
        payload = {'courierId': 0}
        response = requests.get(f"{URL}api/v1/orders", params=payload)

        assert 404 == response.status_code
        assert '{"code":404,"message":"Курьер с идентификатором 0 не найден"}' == response.text