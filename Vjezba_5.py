import requests

params = {
"id": 'Marin'
}


response = requests.delete('http://192.168.194.5/temperatura', params=params)

print(response.text)
print(response.status_code) 