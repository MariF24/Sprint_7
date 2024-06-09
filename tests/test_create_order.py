import pytest
import allure
import json
import requests
from config import URL

class TestCreateOrder:
    @allure.title('Успешное создание заказа с разными параметрами цвета самоката')
    @pytest.mark.parametrize('color', [["BLACK", "GREY"], ["BLACK"], ["GREY"], [], [""]])
    def test_create_order_true(self, color):
        payload = {
             "firstName": "Naruto",
             "lastName": "Uchiha",
             "address": "Konoha, 142 apt.",
             "phone": "+7 800 355 35 35",
             "rentTime": 5,
             "deliveryDate": "2020-06-06",
             "comment": "Saske, come back to Konoha",
             "color": color
        }

        payload_string = json.dumps(payload)

        response = requests.post(f"{URL}/api/v1/orders", data=payload_string)

        assert 201 == response.status_code
        assert 'track' in response.text






