from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from modules.db_controller import Controller
from modules.logger import log


db = Controller()
app = FastAPI()

class DatabaseEntry(BaseModel):
    nombre : str 
    apellido : str
    telefono : str
    dispositivos_asociados : str
    edad : int
    

@app.get("/")
async def root() -> None:
    return {'Status', 'Ok'}

@app.get("/register")
async def register() -> None:
    ... 

# http://127.0.0.1:8000/login?nombre=giuliano&apellido=crenna&mail=giulicrenna@gmail.com&telefono=214263&edad=63
@app.post("/login")
async def login(nombre : str, apellido : str, telefono : str, edad : int, dispositivo_asociado : str) -> None:
    db.add_entry(nombre=nombre,
                         apellido=apellido,
                         edad=edad,
                         telefono=telefono,
                         dispositivo_asociado=dispositivo_asociado)
    
    
    return {'Status', 'Ok'}
