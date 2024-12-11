import requests

params = {
"username": 'PURS',
"password": '1234'
}


response = requests.get('http://192.168.194.5/login', params=params)

print(response.text)
print(response.status_code) 