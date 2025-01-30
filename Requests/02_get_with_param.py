import requests

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', data=data)
print(response.json())  # Assuming the response is in JSON format
