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
        fields = json.loads(result.text)        # преобразует строку в формат json
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print("Все поля присутствуют")