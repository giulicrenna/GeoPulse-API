import requests
import json

new_user : dict = {
    'nombre' : 'Silvina',
    'apellido' : 'Jurado',
    'dispositivo_asociado' : 'ar1433',
    'telefono' : '+5 2-24544',
    'edad' : 48
}

URL : str = 'http://127.0.0.1:8000/login'

response = requests.post(URL, params=new_user)

print(response.text)