import requests


class TestGetAllJokesFromCategory():
    """"Тест на получение по одной шутке из каждой категории"""

    url = "https://api.chucknorris.io/jokes/categories"

    def __init__(self):
        pass


    def test_get_categories(self, expected_status_code):
        """"Получение списка категорий"""

        result_request = requests.get(self.url)
        response_json = result_request.json()
        print(f"Получение списка категорий: \n{response_json}")

        current_status_code = result_request.status_code
        print(f"\nСтатус код: {current_status_code}")

        assert current_status_code == expected_status_code, f'ОШИБКА!!! Ожидается код {expected_status_code}'
        print("Статус-код корректен\n")


    def test_get_one_joke_from_each_category(self, expected_status_code):
        """"Получение по одной рандомной шутке по каждой существующей категории"""

        result_request = requests.get(self.url)
        response_json = result_request.json()

        for category in response_json:

            print("---------------НАЧАЛО ЗАПРОСА---------------------")

            print(f'Категория: {category}')
            url = f'https://api.chucknorris.io/jokes/random?category={category}'
            print(f'URL-путь: {url}')

            result_request = requests.get(url)
            response_json = result_request.json()

            print(f"Результат запроса в виде json: \n{response_json}\n")

            print(f"Статус код запроса: {result_request.status_code}")
            assert result_request.status_code == expected_status_code, f'ОШИБКА!!! Ожидается код {expected_status_code}'
            print("Статус-код корректен\n")

            joke_value = response_json.get("value")
            print(f"Шутка: \n{joke_value}")
            print("---------------КОНЕЦ ЗАПРОСА---------------------\n")




test1 = TestGetAllJokesFromCategory()

test1.test_get_categories(200)
test1.test_get_one_joke_from_each_category(200)
