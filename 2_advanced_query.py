import requests

print("\n return 1 result\n")
print(requests.get("http://127.0.0.1:8000/items/1").json())

print("\n return 1 result\n")
print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

print("\n query for count = 20 returns 2 results\n")
print(requests.get("http://127.0.0.1:8000/items?count=20").json())

print("\n query for count = 100 returns 1 results\n")
print(requests.get("http://127.0.0.1:8000/items?name=Nails&count=100").json())

print("\n query for count = 1001 returns None\n")
print(requests.get("http://127.0.0.1:8000/items?name=Nails&count=1001").json())
