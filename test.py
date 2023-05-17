import requests
import json

URL_REGISTER : str = 'http://127.0.0.1:8000/register'
URL_DELETE : str = 'http://127.0.0.1:8000/login'
URL_VALIDATION : str = 'http://127.0.0.1:8000/validate'
URL_AVAILABILITY : str = 'http://127.0.0.1:8000/availability'
URL_REPORT : str = 'http://127.0.0.1:8000/report'
URL_DATA : str = 'http://127.0.0.1:8000/data'

new_user : dict = {
    'type' : 'other',
    'username' : 'Irma',
    'fullname' : 'Irma Mirabelli',
    'mail' : 'irma@gmail.com',
    'password' : 'jhuiashkjdhaushd'
}

delete_user : dict = {
    'column' : 'id',
    'id' : 5,
}


#response = requests.post(URL_DELETE, params=delete_user)
response = requests.get(URL_REGISTER, params=new_user)

print(response.text)