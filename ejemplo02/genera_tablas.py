from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
	
Base = declarative_base()

class Provincia(Base):
    __tablename__ = 'provincia'

    codigo_division_prov = Column(Integer, primary_key=True)
    nombre_provincia = Column(String(200))
    cantones = relationship("Canton", back_populates="provincia")
    
    def __repr__(self):
        return "Provincia: Código División Política Administrativa Provincia = %d Nombre Provincia= %s" % (
                          self.codigo_division_prov,
                          self.nombre_provincia)
    
    def obtener_numero_docentes(self):
        suma = 0
        for s in self.cantones:
            for i in s.parroquias:
                for x in i.establecimientos:
                    suma = suma + x.numero_docentes
        return suma
    
    def obtener_lista_parroquias(self):
        lista = []
        for s in self.cantones:
            for i in s.parroquias:
                lista.append(i.nombre_parroquia)
        return lista
    
class Canton(Base):
    __tablename__ = 'canton'

    codigo_division_cant = Column(Integer, primary_key=True)
    nombre_canton = Column(String(200))
    codigo_provincia = Column(Integer, ForeignKey('provincia.codigo_division_prov'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    
    def __repr__(self):
        return "Provincia: Código División Política Administrativa  Cantón = %d Nombre Parroquia =%s" % (
                          self.codigo_division_cant,
                          self.nombre_canton)
    
    def obtener_numero_estudiantes(self):
        suma = 0
        for s in self.parroquias:
            for i in s.establecimientos:
                suma = suma + i.numero_estudiantes
        return suma

    
class Parroquia(Base):
    __tablename__ = 'parroquia'

    codigo_division_parro = Column(Integer, primary_key=True)
    nombre_parroquia = Column(String(200))
    codigo_canton = Column(Integer, ForeignKey('canton.codigo_division_cant'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    
    def __repr__(self):
        return "Parroquia: Código División Política Administrativa Parroquia = %d Nombre Parroquia =%s" % (
                          self.codigo_division_parro,
                          self.nombre_parroquia)
    
    def obtener_numero_establecimientos(self):
        return len(self.establecimientos)
    
    def obtener_tipos_jornada(self):
        lista = []
        for s in self.establecimientos:
            lista.append(s.jornada)
        listaN = list(set(lista))
        return listaN


class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    codigo_AMIE = Column(String(20), primary_key=True)
    nombre_Institucion = Column(String(200))
    zona_administrativa = Column(String(200))
    denominacion_distrito = Column(String(200))
    codigo_distrito = Column(String(200))
    codigo_circuito_educativo = Column(String(200))
    sostenimiento = Column(String(200))
    regimen_escolar = Column(String(200))
    jurisdiccion = Column(String(200))
    tipo_educacion = Column(String(200))
    modalidad = Column(String(200))
    jornada = Column(String(200))
    nivel = Column(String(200))
    etnia = Column(String(200))
    acceso_terrestre_fluvial = Column(String(200))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(200))
    codigo_parroquia = Column(Integer, ForeignKey('parroquia.codigo_division_parro'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: Código AMIE = %s Nombre de la Institución Educativa =%s Zona Administrativa =%s \
Denominación del Distrito =%s Código de Distrito =%s Código de Circuito Educativo =%s Sostenimiento =%s \
Régimen Escolar =%s Jurisdicción =%s Tipo de Educación =%s Modalidad =%s Jornada =%s Nivel =%s Etnia =%s \
Acceso (terrestre/ aéreo/fluvial) =%s Número de estudiantes =%d Número de docentes =%d Estado =%s" % (
                          self.codigo_AMIE,
                          self.nombre_Institucion,
                          self.zona_administrativa,
                          self.denominacion_distrito,
                          self.codigo_distrito,
                          self.codigo_circuito_educativo,
                          self.sostenimiento,
                          self.regimen_escolar,
                          self.jurisdiccion,
                          self.tipo_educacion,
                          self.modalidad,
                          self.jornada,
                          self.nivel,
                          self.etnia,
                          self.acceso_terrestre_fluvial,
                          self.numero_estudiantes,
                          self.numero_docentes,
                          self.estado)

# Crea todas las tablas definidas en Base en la base de datos
Base.metadata.create_all(engine)