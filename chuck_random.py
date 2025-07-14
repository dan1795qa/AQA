import requests


class Test_new_joke():
    """"Create new joke"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """"Create random joke"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Status code: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Success!!! We got a new jokes!")
        else:
            print("Error!!!")
        result.encoding = "utf-8"
        print(result.text)

        check = result.json()

        check_info = check.get("categories")
        assert check_info == []
        print("Categories is True")

        check_info_value = check.get("value")
        print(check_info_value)

        name = "Chuck"
        if name in check_info_value:
            print("Chuck is present!")
        else:
            print("Chuck is missing!")

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()