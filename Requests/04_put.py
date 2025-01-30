import requests
r = requests.put('https://httpbin.org/put', data={'name': 'John Doe', 'role': 'QA Engineer', 'location': 'Bangalore'})
print(r.text)