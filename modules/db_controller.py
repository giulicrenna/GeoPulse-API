import psycopg2
from .logger import log 

database : str = 'usuarios_test'
user : str = 'postgres'
password : str = 'kirchhoff2002'
server : str = '200.58.121.156'
port : str = '5432'
table : str = 'users'

class Controller:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(database = database,
            user = user,
            password = password,
            host = server,
            port = port)
        self.cursor = self.conn.cursor()
        log(f"[DB] Connection to {server}:{port} has been succesfully stablished.")
        
    def remove_entry(self,
                     column : str,
                     id : int) -> None:
        query : str = f"""DELETE FROM {table} WHERE {column} = {id};"""
        
        try:
            self.cursor.execute(query)
            self.conn.commit()
            log(f"[DB] Entry deleted successfully based on {column}:{id}")
        except Exception as ex:
            log(f"[error] : {ex}")
            return
    
    def add_entry(self,
                  nombre : str,
                  apellido : str,
                  edad : int,
                  telefono : str,
                  dispositivo_asociado : str) -> None:
        
        telefono = telefono.replace(' ', '').replace('+', '').replace('-', '')
        if(telefono[0] != '+' and len(telefono) < 13):
            log(f'[DB {server}]: Bad phone number: {telefono}.')
            return 

        #cursor.execute('SELECT * from table where id = %(some_id)d', {'some_id': 1234})

        query : str = f"""INSERT INTO {table} (
                   edad,
                   nombre,
                   apellido,
                   telefono,
                   dispositivo_asociado) 
                   VALUES (%s, %s, %s, %s, %s);"""
        
        try:
            self.cursor.execute(query, (
                            edad,
                            nombre,
                            apellido,
                            telefono,
                            dispositivo_asociado))
            self.conn.commit()
        except Exception as ex:
            log(f"[error] : {ex}")
            return
        log(f"[DB] Usuario registrado: {nombre} {apellido}")
    
    def close_con(self) -> None:
        self.conn.close()