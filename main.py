import requests

r = requests.get(f"https://nyanpass.com/api/get_count")
r.raise_for_status()
nyanpass = int(r.json()["count"])
print(f"{nyanpass}回")
input()
