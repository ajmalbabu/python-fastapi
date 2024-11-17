import requests

print("Deleting an item:")
print(requests.delete("http://127.0.0.1:8000/items/0").json())
print(requests.get("http://127.0.0.1:8000/").json())