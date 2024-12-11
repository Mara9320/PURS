import requests

response = requests.get('http://ip.jsontest.com/')

print(response.text)