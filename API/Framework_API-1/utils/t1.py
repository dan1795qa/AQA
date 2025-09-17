import json

import requests

url = "https://dog.ceo/api/breed/hound/images"
# headers = {
#     "x-api-key": "reqres-free-v1"
# }
json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]
result = requests.get(url=url,)
fields = json.loads(result.text)

print(result.status_code)
result_json = result.json()
result_dict = dict(result_json)
substring = 'hound-english'
for k, v in result_dict.items():
    if k == 'message':
        list_v = list(v)
        count = sum(1 for item in list_v if substring in item)
        print(count)




# print(result_json)
# for k, v in result_json.items():
#     print(v)