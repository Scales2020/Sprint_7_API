import allure
from helper import TestData
from routes_courier import APIHelp
from user_data import NewData


class TestCourier:
    @allure.title('Проверка, что курьера можно создать: возвращается правильный код (201) и тело ответа (ok:true)')
    def test_new_courier_created(self):
        new_courier_data = TestData.generate_new_courier_data(self)
        new_courier = APIHelp.create_courier(new_courier_data)
        assert new_courier.status_code == 201
        test_message = new_courier.text
        assert '{"ok":true}' in test_message
        courier_id = APIHelp.get_courier_id({"login": new_courier_data["login"], "password": new_courier_data["password"]})
        APIHelp.delete_courier(courier_id)

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_two_similar_couriers_not_created(self):
        new_courier_data = TestData.generate_new_courier_data(self)
        new_courier = APIHelp.create_courier(new_courier_data)
        assert new_courier.status_code == 201
        new_courier_2 = APIHelp.create_courier(new_courier_data)
        assert new_courier_2.status_code == 409
        error_message = new_courier_2.json().get('message')
        assert "Этот логин уже используется" in error_message
        courier_id = APIHelp.get_courier_id({"login": new_courier_data["login"], "password": new_courier_data["password"]})
        APIHelp.delete_courier(courier_id)

    @allure.title('Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_use_of_existing_login_returns_error(self):
        new_courier_1 = APIHelp.create_courier(NewData.new_user_1)
        assert new_courier_1.status_code ==201
        print(f'курьер с логином {NewData.new_user_1["login"]} успешно создан')
        new_courier_2 = APIHelp.create_courier(NewData.new_user_2)
        assert new_courier_2.status_code == 409
        error_message = new_courier_2.json().get('message')
        with allure.step("Сверяем ответ: Этот логин уже используется"):
            assert 'Этот логин уже используется' in error_message
        courier1_id = APIHelp.get_courier_id({"login": NewData.new_user_1["login"], "password": NewData.new_user_1["password"]})
        APIHelp.delete_courier(courier1_id)

    @allure.title('Проверка, что чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_less_than_three_datafields_return_error(self):
        with allure.step('Передаем на вход пустое поле логина'):
            new_courier = APIHelp.create_courier(NewData.new_user_empty)
        assert new_courier.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in new_courier.json().get('message')

