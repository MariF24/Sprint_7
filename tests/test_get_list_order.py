import pytest
import allure
import json
import requests
from config import URL

class TestListOrder:

    @allure.title('Проверка получения списка заказов без указания id курьера')
    def test_get_list_order_true(self):
        response = requests.get(f"{URL}api/v1/orders")

        assert 200 == response.status_code
        assert '{"orders":[' in response.text
