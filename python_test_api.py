import requests

BASE_URL = "http://127.0.0.1:5000/users"


# CREATE (POST)
users_to_create = [
    {"name": "Uma", "email": "u@gmail.com"},
    {"name": "Venkat", "email": "v@gmail.com"}
]

for user in users_to_create:
    response = requests.post(BASE_URL, json=user)
    print("POST:", response.json())


# READ ALL (GET)
response = requests.get(BASE_URL)
print("GET ALL:", response.json())


# UPDATE USER 1 (PUT)
update_data = {
    "name": "Uma Updated"
}
response = requests.put(f"{BASE_URL}/1", json=update_data)
print("PUT:", response.json())


# READ SINGLE USER (GET)
response = requests.get(f"{BASE_URL}/1")
print("GET ONE:", response.json())


# DELETE USER 2 (DELETE)
response = requests.delete(f"{BASE_URL}/2")
print("DELETE:", response.json())


# FINAL READ
response = requests.get(BASE_URL)
print("FINAL DATA:", response.json())