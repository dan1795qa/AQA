import requests
import os

class FiveNewLocations():

    base_url = "https://rahulshettyacademy.com"  # Базовая url
    key = "?key=qaclick123"  # Параметр для всех запросов

    def __init__(self):
        pass

    """"Очистка файла с локациями"""
    def clear_file(self):

        with open("last_five_locations.txt", "w") as file:
            pass

        print("Файл очищен")


    """"Создание 5(пяти) новых локаций и запись place_id в файл file_api_place_id.txt"""
    def test_create_new_location(self):

        """"Создание новой локации"""
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        post_url = self.base_url + post_resource + self.key
        print(post_url)

        count_requests = 1

        while count_requests < 6:
            print(f"\n-----------Запрос номер {count_requests}----------------")
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            result_post = requests.post(post_url, json=json_for_create_new_location)
            print(result_post.text)

            print("Статус код: " + str(result_post.status_code))
            assert 200 == result_post.status_code
            print("Успешно!!! Cоздана новая локация")

            check_post = result_post.json()
            check_info_post = check_post.get("status")
            print(check_info_post)
            print("Статус код ответа: " + check_info_post)
            assert check_info_post == "OK"
            print("Статус ответа верен")
            place_id = check_post.get("place_id")
            print("Place_id: " + place_id)

            with open("last_five_locations.txt", "a") as file:
                file.write(place_id + "\n")

            count_requests += 1



    def test_check_locations_from_file(self):
        """"Проверка создания пяти локаций"""
        file_path = 'last_five_locations.txt'

        if os.path.getsize(file_path) != 0:
            print("Файл не пустой")

            with open(f"{file_path}", 'r') as file:
                content = file.read()
                list_place_id = content.rstrip().split('\n')
                print(list_place_id)

            for place_id in list_place_id:
                print(f"\n-----------Запрос для place_id: {place_id}----------------")
                get_resource = "/maps/api/place/get/json"
                get_url = self.base_url + get_resource + self.key + '&place_id=' + place_id
                print(get_url)
                result_get = requests.get(get_url)
                print(result_get.text)

                print("Статус код: " + str(result_get.status_code))
                assert 200 == result_get.status_code
                print("Успешно!!! Проверка создания новой локации прошла успешно")

        else:
            print("Файл пустой!!!")






test = FiveNewLocations()
test.test_create_new_location()
test.test_check_locations_from_file()
#
# test.clear_file()