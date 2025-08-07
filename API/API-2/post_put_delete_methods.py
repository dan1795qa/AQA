import requests

class New_location():
    """"Работа с новой локацией"""

    def test_create_new_location(self):
        """"Создание новой локации"""

        base_url = "https://rahulshettyacademy.com"                     # Базовая url
        key = "?key=qaclick123"                                          # Параметр для всех запросов

        """"Создание новой локации"""
        post_resource = "/maps/api/place/add/json"                      # Ресурс метода Post

        post_url = base_url + post_resource + key
        print(post_url)

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
        print("Статус код ответа: " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")
        place_id = check_post.get("place_id")
        print("Place_id: " + place_id)

        print('-'*150)



        """"Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print("Статус код: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        print("Успешно!!! Проверка создания новой локации прошла успешно")

        print('-'*150)


        """"Изменение новой локации"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)

        print("Статус код: " + str(result_put.status_code))
        assert 200 == result_put.status_code
        print("Успешно!!! Изменение новой локации прошла успешно")

        check_put = result_put.json()
        check_info_put = check_put.get("msg")
        print("Сообщение: " + check_info_put)
        assert check_info_put == "Address successfully updated"
        print("Статус ответа верен")

        print('-'*150)



        """"Проверка изменения новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)

        print("Статус код: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        print("Успешно!!! Проверка изменения новой локации прошла успешно")

        check_address = result_get.json()
        check_info_address = check_address.get("address")
        print("Сообщение: " + check_info_address)
        assert check_info_address == "100 Lenina street, RU"
        print("Сообщение верно")

        print('-'*150)


        """"Удаление новой локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id
        }

        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print(result_delete.text)

        print("Статус код: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        print("Успешно!!! Проверка удаления новой локации прошла успешно")

        check_status = result_delete.json()
        check_info_status = check_status.get("status")
        print("Сообщение: " + check_info_status)
        assert check_info_status == 'OK'
        print("Сообщение верно")

        print('-' * 150)

        """"Проверка удаления новой локации"""

        result_get = requests.get(get_url)
        print(result_get.text)

        print("Статус код: " + str(result_get.status_code))
        assert 404 == result_get.status_code
        print("Успешно!!! Проверка удаления новой локации прошла успешно")

        check_msg = result_get.json()
        check_info_msg = check_msg.get("msg")
        print("Сообщение: " + check_info_msg)
        assert check_info_msg == "Get operation failed, looks like place_id  doesn't exists"
        print("Сообщение верно")

        print('-' * 150)





new_place = New_location()
new_place.test_create_new_location()