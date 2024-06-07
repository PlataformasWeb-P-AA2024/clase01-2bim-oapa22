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
cantones = session.query(Canton).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("A cada cantón pedirle el número de estudiantes")
for s in cantones:
    print("Cantón: %s - Número de estudiantes: %d" % (s.nombre_canton, s.obtener_numero_estudiantes())) 
    print("---------")

