import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# load the .env file variables
load_dotenv()

def db_connect():
    # Leer la URL de la base de datos desde la variable de entorno
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL no está configurada en el archivo .env")
    engine = create_engine(database_url)
    return engine
