import allure
import pytest
from routes_courier import APIHelp
from user_data import NewData


class TestloginCourier:
    @pytest.mark.parametrize('var_auth', [{"password": NewData.new_user_log["password"]},
                                          {"login": NewData.new_user_log["login"]},
                                          {"login": "", "password": ""}])

    @ allure.title('Проверка, что для входа нужно передать все обязательные поля (параметризация, 3 варианта)')
    def test_less_than_two_datafields_fails_to_login(self, var_auth):
        APIHelp.create_courier(NewData.new_user_log)
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        login_response = APIHelp.login_courier(var_auth)
        with allure.step('передаем не все обязательные поля, вход не удается:'):
            print(login_response.status_code)
            print(login_response.text)
        assert login_response.status_code == 400 or 504
        APIHelp.delete_courier(courier_id)


    @allure.title('Поверка, что курьер может авторизоваться')
    def test_courier_login_success(self):
        APIHelp.create_courier(NewData.new_user_log)
        login_response = APIHelp.login_courier({"login": NewData.new_user_log["login"],"password": NewData.new_user_log["password"]})
        assert login_response.status_code == 200
        print(login_response.status_code)
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"],"password": NewData.new_user_log["password"]})
        APIHelp.delete_courier(courier_id)

    @allure.title('Проверка, что успешный запрос возвращает id')
    def test_courier_login_returns_id(self):
        APIHelp.create_courier(NewData.new_user_log)
        login_response = APIHelp.login_courier({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        assert '"id":' in login_response.text
        print(login_response.text)
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        APIHelp.delete_courier(courier_id)

    @allure.title('Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_not_existing_courier_login_return_error(self):
        APIHelp.create_courier(NewData.new_user_log)
        APIHelp.login_courier({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        APIHelp.delete_courier(courier_id)
        login_response = APIHelp.login_courier({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        assert login_response.status_code == 404
        with allure.step('Ответ на попытку авторизоваться под несуществующим(удаленным) пользователем:'):
            print(login_response.text)


    @allure.title('Проверка, что если какого-то поля нет, запрос возвращает ошибку')
    def test_less_than_two_datafields_returns_error(self):
        APIHelp.create_courier(NewData.new_user_log)
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        login_response = APIHelp.login_courier({"login": "", "password": NewData.new_user_log["password"]})
        assert login_response.status_code == 400
        print(login_response.status_code)
        APIHelp.delete_courier(courier_id)

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль')
    def test_incorrect_login_or_passw_returns_error(self):
        APIHelp.create_courier(NewData.new_user_log)
        courier_id = APIHelp.get_courier_id({"login": NewData.new_user_log["login"], "password": NewData.new_user_log["password"]})
        login_response = APIHelp.login_courier({"login": "Murmur", "password": NewData.new_user_log["password"]})
        assert login_response.status_code == 404
        print(f'Некорректный логин или пароль, ошибка {login_response.status_code}')
        APIHelp.delete_courier(courier_id)


