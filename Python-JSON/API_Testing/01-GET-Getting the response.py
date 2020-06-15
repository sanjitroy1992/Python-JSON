"""
This is a simple Get request example
api testing site: https://reqres.in
"""
import requests
import json
base_url = "https://reqres.in"
response = requests.get(base_url +"/api/users?page=2")
assert response.status_code == 200
pretty_print = json.dumps(response.json(), indent=2)
print(pretty_print)