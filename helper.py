import allure
import random
import string

class TestData:
    @allure.step('Готовим набор рандомных данных')
    def generate_new_courier_data(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}
        return payload
