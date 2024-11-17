import requests

print("Updating an item:")
print(requests.put("http://127.0.0.1:8000/items/0?count=9001").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()