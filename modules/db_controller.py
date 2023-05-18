import mysql.connector
import random

from .logger import log 
from .configs import *
"""
============= TABLAS =============
users:
-username
-fullname
-mail
-password

reports:
-uuid
-timestamp
-latitude
-longitude

devices:
-mail
-uuid

payment:
-mail
-expiration_date
-expiration_status
-credit_card_number
-credit_card_fullname
-credit_card_pin
-credit_card_expiration_date

temporal:
-mail
-pin
"""


class Controller:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(
            host = server,
            user = user,
            password = password,
            database = database
        ) 
        
        if self.conn:
            log(f"[DB] Connection to {server}:{port} has been succesfully stablished.")
        else:
            log(f"[DB] Connection to {server}:{port} failed.")
        
        self.cursor = self.conn.cursor()
    
    def get_data(self,
                 key : str,
                 table : str) -> list:
        query : str = f"SELECT {key} FROM {table}"
        
        self.cursor.execute(query)
        data : list = self.cursor.fetchall()
        data = [x[0] for x in data]
       
        return data
    
    def remove_entry(self,
                     column : str,
                     id : int) -> None:
        query : str = f"""DELETE FROM {column} WHERE {column} = {id};"""
        
        try:
            self.cursor.execute(query)
            self.conn.commit()
            log(f"[DB] Entry deleted successfully based on {column}:{id}")
        except Exception as ex:
            log(f"[error] : {ex}")
            return
    
    def generate_pin(self) -> str:
        pin : str = ""
        
        for i in range(6):
            pin += str(random.randint(0, 9))
        
        log(f"[DB] New pin generated : {pin}")
        return pin
    """
    This function add a new pin into temporal 
    data for the account verification
    """
    def add_registration_attempt(self,
                                 mail : str) -> str:
        
        register_pins : str = self.get_data("pin", "temporal")
        pin : str = self.generate_pin()
        
        while pin in register_pins or pin == "000000":
            pin = self.generate_pin()
            
        query : str = "INSERT INTO temporal (mail, pin) \
            values (%s, %s)" 
        values : tuple = (mail, pin)
        
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            
        except Exception as e:
            log(f"[DB] Exception: {e}")
            return "000000"
            
        log(f"[DB] Pin : {pin} given to {mail}")
        return pin
    
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

        query : str = f"""INSERT INTO {conf.table} (
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