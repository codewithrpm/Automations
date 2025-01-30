import requests

response = requests.get('https://api.github.com/events')
print(response.status_code)  # prints HTTP status code
print(response.text)         # prints the response body as a string