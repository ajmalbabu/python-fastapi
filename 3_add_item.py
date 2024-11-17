import requests

print("Adding an item:")
print(
    requests.post(
        "http://127.0.0.1:8000/",
        
        json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": "tools"},
    ).json()
)
print(requests.get("http://127.0.0.1:8000/").json())