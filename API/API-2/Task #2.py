import requests
import os


class DeleteSomeLocations():

    file_path = 'last_five_locations.txt'
    base_url = "https://rahulshettyacademy.com"  # Базовая url
    key = "?key=qaclick123"  # Параметр для всех запросов

    def __init__(self):
        pass


    """"Очистка файла с локациями"""

    def clear_file(self):

        with open("new_last_five_locations.txt", "w") as file:
            pass

        print("Файл очищен")


    def test_delete_location(self):
        """"Удаление новой локации"""

        if os.path.getsize(self.file_path) != 0:
            print("Файл не пустой")

            delete_resource = "/maps/api/place/delete/json"
            delete_url = self.base_url + delete_resource + self.key
            print(delete_url)

            with open("last_five_locations.txt", 'r')as file:
                content = file.read()
                list_place_id = content.rstrip().split('\n')

            for place_id in list_place_id:

                if place_id == list_place_id[1] or place_id == list_place_id[3]:

                    print(f"\n--------------Удаление локации с place_id: {place_id}---------------------")
                    json_for_delete_new_location = {
                        "place_id": place_id
                    }

                    result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
                    print(result_delete.text)

                    print("Статус код: " + str(result_delete.status_code))
                    assert 200 == result_delete.status_code
                    print("Успешно!!! Проверка удаления локации прошла успешно")

                    check_status = result_delete.json()
                    check_info_status = check_status.get("status")
                    print("Сообщение: " + check_info_status)
                    assert check_info_status == 'OK'
                    print("Сообщение верно")

        else:
            print("Файл пустой!!!")

        print('-' * 150)


    def test_check_locations_and_create_new_file(self):
        """"Проверка существования пяти локаций и создание нового актуального файла с существующеми place_id"""

        if os.path.getsize(self.file_path) != 0:
            print("Файл не пустой")

            with open(f"{self.file_path}", 'r') as file:
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

                if result_get.status_code == 200:
                    with open("new_last_locations.txt", "a") as file:
                        file.write(place_id + "\n")
                    print(f"Успешно!!! Локация с place_id {place_id} существует")
                    print(f"Локация с place_id {place_id} добавлена в файл new_last_locations")
                elif result_get.status_code == 404:
                    print(f"Ошибка!!! Локация с place_id {place_id} не существует")

        else:
            print("Файл пустой!!!")



test = DeleteSomeLocations()
test.test_delete_location()
test.test_check_locations_and_create_new_file()
# test.clear_file()