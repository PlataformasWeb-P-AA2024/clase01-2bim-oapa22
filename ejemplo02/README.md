# Trabajo Final Primer Bimestre

## Uso de SqlAlchemy

Dada la información de la carpeta ***data***. Realizar las siguientes tareas:

* Analizar el contenido

* Identificar las posibles entidades que se puedan generar

* La base de datos que se debe usar es mysql; el nombre de la base de datos es **final1bim**

* Las entidades deben satisfacer lo siguiente:
	* Un establecimiento tiene características propias.
	* Un establecimiento pertenece a una parroquia.
	* Una parroquia pertenece a un cantón.
	* Un cantón pertenece a un provincia.

* Generar un proceso de generación de entidades a través de SqlAlchemy.
	* crear_tablas.py

* Ingresar la información en cada entidad creada.
	* genera_provincias.py
	* genera_cantones.py
	* genera_parroquias.py
	* genera_establecimientos.py

* Generar las siguientes consultas:
	* datos1.py
		* Todos los establecimientos que pertenecen al Código División Política Administrativa  Parroquia con valor 020151 y 020153
	* datos2.py
		* Todos los establecimientos de la provincia de Bolivar.
	* datos3.py
		* Todos los establecimientos del cantón de Guayaquil.
	* datos4.py
		* Todos los establecimientos del cantón de Urdaneta y Vinces.
	* datos5.py
    	* Las parroquias que tienen establecimientos únicamente en la jornada "Matutina, Vesperina y Nocturna"
	* datos6.py
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100
	* datos7.py
		* Los cantones que tiene establecimientos con 0 número de profesores y 210 estudiantes
	* datos8.py
		* Los establecimientos que tienen como parte de nombre la cadena "UNIDOS"
	* datos9.py
			* Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.
	* datos11.py
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 090112.
	* datos12.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores y régimen escolar igual Sierra.
	* datos13.py
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores y régimen escolar igual Costa.
