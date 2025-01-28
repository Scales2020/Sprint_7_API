import json
import allure
import pytest
from routes_order import APIOrder


class TestOrder:
    @pytest.mark.parametrize('color', [(["GREY"]),
        (["BLACK"]),
        (["GREY", "BLACK"]),
        ([])
    ])
    @allure.title('Проверка создания заказа с параметризацией по цвету самоката')
    def test_create_new_order_successful_with_track(self, color):
        order_data ={
            "firstName": "SemenSemenych",
            "lastName": "Gorbunkov",
            "address": "Dubrovka, 22",
            "metroStation":"4",
            "phone": "+7 800 222 22 22",
            "rentTime": "5",
            "deliveryDate": "2025-02-02",
            "comment": "better you come to us",
            "color": color
        }
        order_data=json.dumps(order_data)
        response = APIOrder.create_new_order(order_data)
        with allure.step(f'Полные данные для заказа {order_data}'):
            assert response.status_code == 201
        with allure.step(f'Тело ответа содержит track - {response.text}'):
            assert "track" in response.text


