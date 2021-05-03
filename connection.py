from mysql.connector import connect 
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def returnConnection():
    conn = connect(
        host = getenv('DB_HOST'),
        user = getenv('DB_USER'),
        password = getenv('DB_PASSWORD'),
        database = getenv('DB_DATABASE')
    )
    return conn


