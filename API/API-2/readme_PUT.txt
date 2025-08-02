Learning the basics of automated API testing





Метод PUT

Запрос:

Base URL: https://rahulshettyacademy.com

Resource: /maps/api/place/update/json

Параметр для запросов: key=qaclick123

Body:

{ 

"place_id":"c104d917f4b60e2c9a5feda6c9cbf279",

 "address":"100 Lenina street, RU", 

"key":"qaclick123" 

}

 

Ответ:

Статус: 200. Запрос прошел успешно

{

    "msg": "Address successfully updated"

}

 

Статус: 404. Ошибка, локация с таким place_id отсутствует

{

    "msg": "Update address operation failed, looks like the data doesn't exists"

}
