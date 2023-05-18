import mysql.connector
from modules.logger import log
import modules.configs as conf


def createTables() -> None:
    conn = mysql.connector.connect(
        host = conf.server,
        user = conf.user,
        password = conf.password,
        database = conf.database
    )
    
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS users \
        (id INT AUTO_INCREMENT PRIMARY KEY, \
            username VARCHAR(100) UNIQUE, \
                fullname VARCHAR(100), \
                    mail VARCHAR(100) UNIQUE, \
                        password VARCHAR(100))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS reports \
        (uuid VARCHAR(100), \
            timestamp VARCHAR(100), \
                latitude VARCHAR(100), \
                    longitude VARCHAR(100))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS devices \
        (uuid VARCHAR(100) UNIQUE, \
            mail VARCHAR(100))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS payment \
        (mail VARCHAR(100) UNIQUE, \
            credit_card_number VARCHAR(100) UNIQUE, \
                credit_card_fullname VARCHAR(100), \
                    credit_card_pin VARCHAR(100), \
                        credit_card_expiration_date VARCHAR(100), \
                            expiration_date VARCHAR(100), \
                                expiration_status VARCHAR(100))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS temporal \
        (mail VARCHAR(100) UNIQUE, \
            pin VARCHAR(6))")
    
    
    
    
if __name__ == '__main__':
    createTables()