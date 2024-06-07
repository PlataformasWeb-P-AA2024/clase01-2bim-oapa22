from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Parroquia,Canton

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# acceder al archivo
archivo = open('data/Listado-Instituciones-Educativas-02.csv', "r")

# obtener las líneas del archivo
data = archivo.readlines()
archivo.close()

for lineas in data[1:]:

    linea = lineas.strip().split("|")

    # Buscar el canton existente
    existe_canton = session.query(Canton).filter_by(codigo_division_cant=linea[4]).first()
    
    # Verificar si la parroquia ya existe
    existe_parroquia = session.query(Parroquia).filter_by(codigo_division_parro=linea[6]).first()

    if not existe_parroquia:
        parroquia = Parroquia(codigo_division_parro=linea[6], nombre_parroquia=linea[7], canton=existe_canton)
        session.add(parroquia)
    

session.commit()

