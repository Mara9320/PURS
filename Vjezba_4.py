import requests

payload = {
"temperatura": '44'
}


response = requests.post('http://192.168.194.5/temperatura', json=payload)

print(response.text)
print(response.status_code) 