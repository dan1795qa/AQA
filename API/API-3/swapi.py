import json

import requests


class Swapi_heroes():

    def test_get_characters(self):

        global list_films, list_characters, list_name_characters, character

        """"Получение списка всех фильмов где снимался Дарт Вейдер"""
        base_url = "https://swapi.dev/api/"
        resource = "people/4/"
        get_url = base_url + resource
        print(get_url)
        result = requests.get(get_url, verify=False)
        result_get_json = result.json()
        print(result_get_json)

        for k, v in dict(result_get_json).items():
            if k == 'films':
                list_films = v
                print(list_films)

        """"Получение списка персонажей, которые снимались с Дарт Вейдером в фильмах полученных ранее"""
        for i in list_films:
            list_characters = []
            result_get_characters = requests.get(i, verify=False)
            result_get_characters_json = result_get_characters.json()
            for k, v in dict(result_get_characters_json).items():
                if k == 'characters':
                    list_characters = list_characters + v

        list_name_characters = []
        for i in list_characters:
            character = requests.get(i, verify=False).json().get('name')
            list_name_characters.append(character)

        """"Запись полученного списка персонажей в отдельный файл"""
        print(list_name_characters)
        with open('./answer.txt', 'w', encoding='utf-8') as answer:
            for i in list_name_characters:
                answer.write(f"{i}\n")


test = Swapi_heroes()
test.test_get_characters()
