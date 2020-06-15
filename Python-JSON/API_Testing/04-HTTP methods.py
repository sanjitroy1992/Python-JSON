"""
This is a GET request for Adding Query parameters to requests
api testing site: https://reqres.in
"""
import requests
base_url = "https://reqres.in"
## 01 GET Request
params = {"page":2}
response = requests.get(base_url + "/api/users?", params=params)
assert response.status_code == 200
print("GET - Passed")

## 02 POST Request
post_payload = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post(base_url + "/api/users", data=post_payload)
assert response.status_code == 201
print("POST - Passed")

## 03 PUT Request
put_payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put(base_url + "/api/users/2", data=put_payload)  # Notice here we are updating user 2 in the uri
assert response.status_code == 200
print("PUT - Passed")

## 04 DLELETE Request
response = requests.delete(base_url + "/api/users/2")  # Notice here we are deleting user 2.
# Usually after post request we get the list of user ids and we parser the id for the user to be deleted.
assert response.status_code == 204
print("DELETE - Passed")