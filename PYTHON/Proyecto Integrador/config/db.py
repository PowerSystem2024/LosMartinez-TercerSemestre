# db.py
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Cargar las variables de entorno
load_dotenv()

# Obtener configuraciones de la base de datos desde las variables de entorno
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Crear la URL de conexión para SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Crear el motor de conexión de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Verificar la conexión
with session:
    try:
        # Ejecutamos una simple consulta de prueba para verificar la conexión
        result = session.execute(text("SELECT 1"))
        print(f"Conexión exitosa, la base de datos responde: {result.fetchone()}")
    except Exception as e:
        session.rollback()
        print(f"Error en la conexión: {e}")
    finally:
        # Cerrar la sesión
        session.close()