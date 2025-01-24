import allure
import requests
from constants import Constants


class APIHelp:
    @allure.step('Создаем нового курьера')
    def create_courier(data):
        return requests.post(f'{Constants.C_URL}', data=data)

    @allure.step(f'Удаляем созданного курьера')
    def delete_courier(courier_id):
        return requests.delete(f'{Constants.C_URL}/{courier_id}')

    @allure.step(f'Авторизация созданного курьера')
    def login_courier(data):
        return requests.post(f'{Constants.C_URL}/login', data=data)

    def get_courier_id(data):
        response = APIHelp.login_courier(data)
        return response.json().get('id')
