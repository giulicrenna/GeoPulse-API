from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

import time
import calendar

from modules.decryptor import decrypt
from modules.db_controller import Controller
from modules.logger import log

#  uvicorn main:app --reload

#db = Controller()  
app = FastAPI()

app.mount("/test", StaticFiles(directory="./server/", html=True), name="API test")


@app.get("/")
async def root() -> None:
     return {'status' : 'ok'}
     
@app.get("/register")
async def auth(type :str,
                   username : str,
                   fullname : str,
                   mail : str,
                   password : str) -> None:
    
    
    if type == 'register':
        log(f"[register] {type} : new registration attempt, sending mail to {mail}")
        print('Enviando Mail')
        return {'status' : 'ok'}
    
    elif type == 'login':
        log(f"[login] new login by {mail}")
        print('Logueando') 
        return {'status' : 'ok'}
    
    log(f"[auth] {type} : bad request")
    return {'status' : 'bad'}

@app.get("/data")
async def data(get : str,
               uuid : str,
               mail : str):
    uuid_d : str = decrypt(uuid)
    print(uuid_d)
     
    if get == 'loc':
        return { 
            'uuid' : uuid,
            'latitude' : 87.34453453,
            'longitude' : 34.435435,
            'timestamp' : calendar.timegm(time.gmtime())
        }
    elif get == 'history':
        return {
            'uuid' : uuid,
            'latitude' : [87.34453453, 48.41891651, 87.186161],
            'longitude' : [34.435435, 87.8494465, 84.548964],
            'timestamp' : [calendar.timegm(time.gmtime()), 8498465849845, 46546486]
        }
        
    return {'status' : 'bad'}

@app.get("/report")
async def report(uuid : str,
                 latitude : str,
                 longitude : str,
                 timestamp : str,
                 mail : str):
    
    print(f"Reported: {decrypt(uuid)}")
    print(f"device at:\nLat: {latitude}\nLong: {longitude}")
    
    return {"status" : "reported"}
