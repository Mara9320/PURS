import requests

response = requests.get('http://192.168.194.5/login')

print(response.text)
print(response.status_code) 

for k, v in response.headers.items():
    print(f'{k}: {v}')