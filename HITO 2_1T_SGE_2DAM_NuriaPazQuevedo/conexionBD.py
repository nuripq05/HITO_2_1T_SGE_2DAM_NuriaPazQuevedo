import mysql.connector

class CConexion:
    def __init__(self):
        self.conn = None
        
    def connectionBD(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="campusfp",
                database="ENCUESTAS"
            )
            return self.conn
        except mysql.connector.Error as error:
            print(f"No se pudo conectar: {error}")
    
    def cerrar_conexion(self):
        if self.conn.is_connected():

            self.conn.close()
            print("Conexion cerrada")
