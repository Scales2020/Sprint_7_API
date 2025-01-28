import requests
from constants import Constants


class APIOrder:
    def create_new_order(data):
        return requests.post(f'{Constants.O_URL}', data=data)

    def get_list_of_10_orders(params):
        return requests.get(f'{Constants.O_URL}?limit=10&page=0', params=params)

    def get_list_of_orders_by_station(station_id):
        return requests.get(f'{Constants.O_URL}?limit=10&page=0&nearestStation=["{station_id}"]')


