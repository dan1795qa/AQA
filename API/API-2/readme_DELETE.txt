Learning the basics of automated API testing




Метод DELETE

Запрос:

Base URL: https://rahulshettyacademy.com

Resource: /maps/api/place/delete/json

Параметр для запросов: key=qaclick123

Body:

{

"place_id":"928b51f64aed18713b0d164d9be8d67f"

}

 

Ответ:

Статус: 200. Запрос прошел успешно

{

    "status": "OK"

}

 

Статус: 404. Ошибка, локация с таким place_id отсутствует

{

    "msg": "Delete operation failed, looks like the data doesn't exists"

}

