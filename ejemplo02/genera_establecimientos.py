from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Parroquia,Establecimiento

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

    # Buscar la parroquia existente
    existe_parroquia= session.query(Parroquia).filter_by(codigo_division_parro=linea[6]).first()
    
    existe_establecimiento = session.query(Establecimiento).filter_by(codigo_AMIE=linea[0]).first()

    if not existe_establecimiento:
        establecimeinto = Establecimiento(codigo_AMIE=linea[0], nombre_Institucion=linea[1], zona_administrativa=linea[8], denominacion_distrito=linea[9],\
                                 codigo_distrito=linea[10], codigo_circuito_educativo=linea[11], sostenimiento=linea[12], \
                                 regimen_escolar=linea[13], jurisdiccion=linea[14], tipo_educacion=linea[15], \
                                 modalidad=linea[16], jornada=linea[17], nivel=linea[18], etnia=linea[19], acceso_terrestre_fluvial=linea[20],\
                                 numero_estudiantes=linea[21], numero_docentes=linea[22],  estado=linea[23], parroquia=existe_parroquia)
        session.add(establecimeinto)

session.commit()

