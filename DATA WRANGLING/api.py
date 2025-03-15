import requests

url = 'https://jsonplaceholder.typicode.com/posts'

params = {'id' : 1}

response = requests.get(url, params= params)

# print(response.json())

data = response.json()

userId = data[0]['userId']

userInfo = requests.get('https://jsonplaceholder.typicode.com/users', params= {'id' : userId}).json()

print(userInfo)
