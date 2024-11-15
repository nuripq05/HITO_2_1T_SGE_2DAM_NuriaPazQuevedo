from conexionBD import *

class EEncuestas:

    def __init__(self,conn):
        self.conn = conn

#metodo para agregar una nueva encuesta en la base de datos
    def crear(self,idEncuesta,edad,sexo,bebidasSemana,cervezasSemana,bebidasFinSemana,bebidasDestiladasSemana,vinosSemana, perdidasControl,diversionDependenciaAlcohol,problemasDigestivos,tensionAlta,dolorCabeza):
        try:
            cursor = self.conn.cursor()
            #Define la consulta SQL que quieres realizar
            query = "INSERT INTO encuesta VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (idEncuesta,edad,sexo,bebidasSemana,cervezasSemana,bebidasFinSemana,bebidasDestiladasSemana,vinosSemana, perdidasControl,diversionDependenciaAlcohol,problemasDigestivos,tensionAlta,dolorCabeza)
            cursor.execute(query,values)
            self.conn.commit()
            print("Encuesta agregada")
        except mysql.connector.Error as error:
            print(f"No se puede agregar la encuesta: {error}")
    
#metodo para leer una nueva encuesta en la base de datos

    def leer(self):
        try:
            cursor = self.conn.cursor()
            #Define la consulta SQL que quieres realizar
            query = "SELECT *FROM encuesta"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as error:
            print(f"No se pudo leer las encuestas: {error}")
    
#metodo para actualizar una nueva encuesta en la base de datos

    def actualizar(self, idEncuesta, columna, valor_actualizado):
        try:
            cursor = self.conn.cursor()
            #Define la consulta SQL que quieres realizar
            query = f"UPDATE encuesta SET {columna} = %s WHERE idEncuesta = %s"
            values = (valor_actualizado, idEncuesta)
            cursor.execute(query,values)
            self.conn.commit()
            print("Encuesta actualizada")
        except mysql.connector.Error as error:
            print(f"No se pudo leer las encuestas: {error}")

#metodo para eliminar una nueva encuesta en la base de datos

    def eliminar(self,idEncuesta):
        try:
            cursor = self.conn.cursor()
            #Define la consulta SQL que quieres realizar
            query = "DELETE FROM encuesta WHERE idEncuesta = %s"
            values = (idEncuesta,)
            cursor.execute(query,values)
            self.conn.commit()
            print("Encuesta eliminada")
        except mysql.connector.Error as error:
            print(f"No se pudo leer las encuestas: {error}")

