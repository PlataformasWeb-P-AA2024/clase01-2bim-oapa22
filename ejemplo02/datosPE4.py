from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
provincias = session.query(Provincia).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("A cada provincia preguntar la lista de parroquias")
for s in provincias:
    print("Provincia: %s - Lista de parroquias: %s" % (s.nombre_provincia, s.obtener_lista_parroquias())) 
    print("---------")

