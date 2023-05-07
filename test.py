import requests
import json

new_user : dict = {
    'nombre' : 'Irma',
    'apellido' : 'Mirabelli',
    'dispositivo_asociado' : 'ar1325',
    'telefono' : '+5 2-2455221224424',
    'edad' : 56
}

delete_user : dict = {
    'column' : 'id',
    'id' : 5,
}

URL_REGISTER : str = 'http://127.0.0.1:8000/register'
URL_DELETE : str = 'http://127.0.0.1:8000/delete'

#response = requests.post(URL_DELETE, params=delete_user)
response = requests.post(URL_REGISTER, params=new_user)

print(response.text)