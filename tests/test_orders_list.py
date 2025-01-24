import allure
from routes_order import APIOrder
from user_data import NewData


class TestListOrders:
    @allure.title('Проверка, что в тело ответа возвращается список заказов')
    def test_get_orders_list_by_nearest_station(self):
        with allure.step(f'Вызываем методом GET список заказов по станции метро (код {NewData.station}'):
            results_list = APIOrder.get_list_of_orders_by_station(NewData.station)
        assert results_list.status_code == 200
        assert '"orders":' in results_list.text
        with allure.step('Выводим код ответа и список заказов'):
            print(results_list.status_code)
            print(results_list.text)

