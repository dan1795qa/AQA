import json

import requests


class Checking():
    """"Методы для провекри ответов наших запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def check_json_token(result, expected_value):
        """"Метод для проверки наличия обязательных полей в ответе запроса"""
        fields = json.loads(result.text)  # преобразует строку в формат json
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """"Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"{field_name} верно !!!")

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Слово {search_word} присутствует")