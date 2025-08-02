import requests


class TestGetJokeForUser( ):
    """"Тест на получение шутки в выбранной пользователем категории"""

    url = "https://api.chucknorris.io/jokes/categories"
    name_category_for_user = input('Введите категорию шутки(несколько названий вводите через пробел!!!): ')

    def __init__(self):
        pass


    def test_get_category_for_user(self, expected_status_code):
        """"Получение или не получение шутки по выбранной пользователем категории"""

        result_request = requests.get(self.url)
        response_json = result_request.json()
        # print(f"Получение списка категорий: \n{response_json}")

        current_status_code = result_request.status_code
        print(f"\nСтатус код: {current_status_code}")

        assert current_status_code == expected_status_code, f'ОШИБКА!!! Ожидается код {expected_status_code}'
        print("Статус-код корректен\n")

        name_category_for_user_list = self.name_category_for_user.split(" ")
        for name_category in name_category_for_user_list:
            if name_category in response_json:
                print(f"Категория '{name_category}' существует\n")
                self.test_get_joke_for_user_positive(name_category)
            else:
                print(f"Категория '{name_category}' не существует\n")
                self.test_get_joke_for_user_negative(name_category)


    def test_get_joke_for_user_positive(self, name_category):
        """"Функция на получение шутки существующей категории"""

        print("---------------НАЧАЛО ЗАПРОСА---------------------")

        print(f'Категория: {name_category}')
        url = f'https://api.chucknorris.io/jokes/random?category={name_category}'
        print(f'URL-путь: {url}')

        result_request = requests.get(url)
        response_json = result_request.json()

        print(f"Результат запроса в виде json: \n{response_json}\n")

        print(f"Статус код запроса: {result_request.status_code}")
        assert result_request.status_code == 200, f'ОШИБКА!!! Ожидается код {200}'
        print("Статус-код корректен\n")

        joke_value = response_json.get("value")
        print(f"Шутка: \n{joke_value}")
        print("---------------КОНЕЦ ЗАПРОСА---------------------\n")


    def test_get_joke_for_user_negative(self, name_category):
        """"Функция на получение шутки существующей категории"""

        print("---------------НАЧАЛО ЗАПРОСА---------------------")

        print(f'Категория: {name_category}')
        url = f'https://api.chucknorris.io/jokes/random?category={name_category}'
        print(f'URL-путь: {url}')

        result_request = requests.get(url)
        response_json = result_request.json()

        print(f"Результат запроса в виде json: \n{response_json}\n")

        print(f"Статус код запроса: {result_request.status_code}")
        assert result_request.status_code == 404, f'ОШИБКА!!! Ожидается код {404}'
        print("Статус-код корректен\n")

        joke_value = response_json.get("value")
        print(f"Шутка: \n{joke_value}")

        error = response_json.get("error")
        print(error)
        assert error == 'Not Found', "ОШИБКА, Поле Error некорректно"
        print('Поле Error корректно')

        print("---------------КОНЕЦ ЗАПРОСА---------------------\n")




test1 = TestGetJokeForUser()
test1.test_get_category_for_user(200)
