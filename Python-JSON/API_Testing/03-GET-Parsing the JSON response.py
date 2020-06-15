"""
This is a GET request for Adding Query parameters to requests
api testing site: https://reqres.in
"""
import requests
import json
base_url = "https://reqres.in"
params = {"page":2}
response = requests.get(base_url + "/api/users?", params=params)
assert response.status_code == 200
pretty_print = json.dumps(response.json(), indent=2)
print(pretty_print)
resp = response.json()
inner_list = resp["data"]
for i in range(len(inner_list)):
    print(inner_list[i]["first_name"] + " " + inner_list[i]["last_name"])