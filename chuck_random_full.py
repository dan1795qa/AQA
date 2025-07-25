import requests



class TestCreateRandomeJokeCategory():
    """"Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом по заданной категории"""
    """"https://api.chucknorris.io/jokes/random?category={category}"""

    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_random_joke_category_positive(self, category, expected_status_code):
        """Позитивный тест по получению рандомной шутки по определенной категории, включает:
        отправку запроса, проверка на статус-код, проверка на соответствие категории, печать шутки."""

        path_random_joke_category = f"?category={category}"
        url_full = self.url + path_random_joke_category
        print(f"Полный путь: {url_full}")

        result_request = requests.get(url_full)
        response_json = result_request.json()
        print(f"Результат запроса в виде json: \n{response_json}\n")

        print(f"Статус код запроса: {result_request.status_code}")
        assert result_request.status_code == expected_status_code, f'ОШИБКА!!! Ожидается код {expected_status_code}'
        print("Статус-код корректен\n")

        joke_value = response_json.get("value")
        print(f"Шутка: \n{joke_value}")

        """"Проверка на категорию"""
        joke_category = response_json.get("categories")
        print(joke_category)
        assert joke_category[0] == category, f'ОШИБКА!!! Ожидается категория {category}'
        print('Категория корректна\n')

        #Различные проверки
        print("Тест прошел успешно!!!")
        print("\n------------------------------------------------\n")

    def test_create_random_joke_category_negative(self, category, expected_status_code):
        """Негативный тест по получению рандомной шутки по определенной категории, включает:
        откправку запроса, проверка на статус-код, проверка на соответствие категории, печать шутки."""
        path_random_joke_category = f"?category={category}"
        url_full = self.url + path_random_joke_category
        print(f"Полный путь: {url_full}")

        result_request = requests.get(url_full)
        response_json = result_request.json()
        print(f"Результат запроса в виде json: \n{response_json}\n")

        print(f"Статус код запроса: {result_request.status_code}")
        assert result_request.status_code == expected_status_code, f'ОШИБКА!!! Ожидается код {expected_status_code}'
        print("Статус-код корректен\n")

        joke_value = response_json.get("value")
        print(f"Шутка: \n{joke_value}")

        error = response_json.get("error")
        print(error)
        assert error == 'Not Found', "ОШИБКА, Поле Error некорректно"
        print('Поле Error корректно')

        # Различные проверки
        print("Тест прошел успешно!!!")
        print("\n------------------------------------------------\n")



start_test = TestCreateRandomeJokeCategory()

start_test.test_create_random_joke_category_positive('sport', 200)
start_test.test_create_random_joke_category_negative('an', 404)