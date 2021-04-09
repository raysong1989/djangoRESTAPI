import requests

#url = "http://localhost:9000/api/student_list"
#response = requests.get(url)

url = "http://localhost:9000/api/auth"
response = requests.post(url, data = {'username' : 'ray', 'password' : '1234'})
print(response.text)

myToken = response.json()
token = myToken['token']
header = {'Authorization' : 'Token ' + token}
response = requests.get('http://localhost:9000/api/student_list', headers=header)

print(response.text)
