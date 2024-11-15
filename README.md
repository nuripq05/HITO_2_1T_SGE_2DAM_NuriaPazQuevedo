EXPLICACION CODIGOS COSAS CLAVES:

Importación de librerías
import tkinter as tk #libreria para crear interfaces graficas
import matplotlib.pyplot as plt #Libreria para generar graficos
import pandas as pd #Libreria para trabajar con datos y exportarlos a excel
#Importaciones de los modulos restantes de tkinter
from tkinter import simpledialog #crear cuadros de entraadas simples
from tkinter import messagebox # para cuadros de mensajes emergentes
from CRUD import EEncuestas
from conexionBD import CConexion



tkinter: Biblioteca que permite crear interfaces como ventanas, botones y cuadros de texto.

matplotlib.pyplot: Biblioteca utilizada para generar gráficos.

pandas: Biblioteca que facilita el manejo de datos en tablas y su exportación, por ejemplo, a archivos de Excel.

simpledialog y messagebox: Componentes de tkinter que se utilizan para solicitar información al usuario y mostrar mensajes emergentes.

Inicio de la ventana y conexión a la base de datos
   def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Encuesta de salud y consumo de alcohol")


        self.bd = CConexion()
        self.bd.connectionBD()
        if self.bd.conn:


            self.encuestas = EEncuestas(self.bd.conn)
       
        else:("No se puede conectar a la base de datos")

Se establece una conexión con la base de datos utilizando la clase CConexion. Si la conexión se realiza con éxito, se genera un objeto encuestas que facilita las operaciones en la base de datos vinculadas a las encuestas.





Botones
    #crea los botones en la interfaz
        titulo = tk.Label (self.ventana,text = "Encuestas de salud", font=("Arial", 20))
        titulo.pack(pady=10)


    #botones para las operaciones de agregar,leer,actualizar,eliminar,generar,exportar y filtrar
        self.agregar_boton=tk.Button(self.ventana, text="Agregar Encuesta", command=self.agregar_encuesta)
        self.agregar_boton.pack(pady=5)


        self.ver_boton=tk.Button(self.ventana, text="Ver Encuesta", command=self.ver_encuesta)
        self.ver_boton.pack(pady=5)


        self.actualizar_boton=tk.Button(self.ventana, text="Actualizar Encuesta", command=self.actualizar_encuesta)
        self.actualizar_boton.pack(pady=5)        


        self.eliminar_boton=tk.Button(self.ventana, text="Eliminar Encuesta", command=self.eliminar_encuesta)
        self.eliminar_boton.pack(pady=5)


        self.grafico_boton=tk.Button(self.ventana, text="Generar grafico", command=self.generar_grafico)
        self.grafico_boton.pack(pady=5)


        self.exportacion_boton=tk.Button(self.ventana, text="Exportar a Excel", command=self.exportar_excel)
        self.exportacion_boton.pack(pady=5)


        self.filtrar_boton=tk.Button(self.ventana, text="Filtrar por edad", command=self.filtrar_edad)
        self.filtrar_boton.pack(pady=5)



Se crea una etiqueta que muestra el título "Encuestas de salud" en la ventana. Luego, se añaden varios botones para realizar diferentes acciones como agregar, ver, actualizar y eliminar. El comando self.agregar_encuesta se ejecuta cuando el usuario haga clic en el botón. Este mismo patrón se repite para los otros botones: ,ver, actualizar, eliminar, etc.



Métodos encuesta
agregar
    def agregar_encuesta(self):


#recopila los datos de la encuesta utilizando cuadrs de dialogo
        idEncuesta = simpledialog.askinteger("Agregar Encuesta", "ID de la encuesta:")
        edad = simpledialog.askinteger("Agregar Encuesta", "Edad:")
        sexo = simpledialog.askstring("Agregar Encuesta", "Sexo:")
        bebidasSemana = simpledialog.askinteger("Agregar Encuesta", "Bebidas por semana:")
        cervezasSemana = simpledialog.askinteger("Agregar Encuesta", "Cervezas por semana:")
        bebidasFinSemana = simpledialog.askinteger("Agregar Encuesta", "Bebidas fin semana:")
        bebidasDestiladasSemana = simpledialog.askinteger("Agregar Encuesta", "Bebidas destiladas por semana:")
        vinosSemana = simpledialog.askinteger("Agregar Encuesta", "Vinos por semana:")
        perdidasControl = simpledialog.askinteger("Agregar Encuesta", "Perdidas de control:")
        diversionDependenciaAlcohol = simpledialog.askstring("Agregar Encuesta", "Diversion vs dependencia de alcohol:")
        problemasDigestivos = simpledialog.askstring("Agregar Encuesta", "Problemas digestivos:")
        tensionAlta = simpledialog.askstring("Agregar Encuesta", "Tesion alta:")
        dolorCabeza = simpledialog.askstring("Agregar Encuesta", "Dolor de cabeza:")      


    #llama al metodo crear de EEncuestas para agregar la encuesta
        self.encuestas.crear(idEncuesta,edad,sexo,bebidasSemana,cervezasSemana,bebidasFinSemana,bebidasDestiladasSemana,vinosSemana, perdidasControl,diversionDependenciaAlcohol,problemasDigestivos,tensionAlta,dolorCabeza)
        messagebox.showinfo("Exito", "Encuesta agregada exitosamente.")



simpledialog.askinteger(): Solicita al usuario que introduzca un número entero (como el ID de la encuesta, la edad, etc.).
self.encuestas.crear(): Invoca el método crear de la clase EEncuestas, que añade la encuesta a la base de datos.
messagebox.showinfo(): Presenta un mensaje de éxito que indica que la encuesta se ha agregado correctamente.
ver
   def ver_encuesta(self):
        encuestas = self.encuestas.leer()
        #convierte las encuestas en candenas de texto
        encuestas_texto = "\n".join(map(str,encuestas))
        #muestra las encuestas en un cuadro de mensaje
        messagebox.showinfo("Encuestas", encuestas_texto)



self.encuestas.leer(): Obtiene todas las encuestas almacenadas en la base de datos.
messagebox.showinfo(): Presenta todas las encuestas en un cuadro de diálogo.

-actualizar
   def actualizar_encuesta(self):


        #pide el id, la columna a actualizar y el nuevo valor
        idEncuesta = simpledialog.askinteger("Actualizar Encuesta", "ID de la encuesta a actualizar:")
        columna =simpledialog.askstring("Actualiar encuesta", "Columna a actualizar(Por ejemplo: edad):")
        valor_actualizado = simpledialog.askinteger("Actualizar encuesta", "Nuevo valor:")


    #Llama al metodo actualizar de EEncuestas
        self.encuestas.actualizar(idEncuesta,columna,valor_actualizado)
        messagebox.showinfo("Exito", "Encuesta actualizada exitosamente")

self.encuestas.actualizar(): Actualiza una encuesta específica en la base de datos utilizando el ID, la columna que se desea modificar y el nuevo valor.

eliminar
    def eliminar_encuesta(self):
        idEncuesta = simpledialog.askinteger("Eliminar Encuesta", "ID de la encuesta a eliminar:")
        #Llama al metodo eliminar de EEncuestas
        self.encuestas.eliminar(idEncuesta)
        messagebox.showinfo("Exito", "Encuesta eliminada exitosamente")

self.encuestas.eliminar(): Elimina una encuesta de la base de datos utilizando su ID.



generar gráfico
   def generar_grafico(self):
        encuestas = self.encuestas.leer()
        #coge las edades y la scantidades de bebidas por semana
        edades = [encuesta[1] for encuesta in encuestas]
        bebidas = [encuesta[3] for encuesta in encuestas]


        #crea un grafico de barras
        plt.bar(edades,bebidas)
        plt.xlabel('Edad')
        plt.ylabel('Bebidas por semana')
        plt.title('Consumo de alcohol por edad')
        plt.show()

plt.bar(): Crea un gráfico de barras que muestra la relación entre las edades y la cantidad de bebidas consumidas por semana.

exportar 
   def exportar_excel(self):
        #obtiene las encuestas y define los nombres de las columnas
        encuestas = self.encuestas.leer()
        columnas = ["ID","Edad","Sexo", "Bebidas por semana","Cervezas por semana",
                    "Bebidas destiladas","Vinos por semana","Perdidas de control","Diversion vs dependencia","Problemas digestivos","Tension alta","Dolor de cabeza","Nueva columna"]
        df = pd.DataFrame(encuestas,columns=columnas)
        df.to_excel("encuestas.xlsx", index=False)
        messagebox.showinfo("Exito","Datos exportados exitosamenre")

pandas.DataFrame(): Transforma los datos de las encuestas en una tabla (DataFrame).
df.to_excel(): Exporta los datos a un archivo Excel titulado "encuestas.xlsx".

filtrar
    def filtrar_edad(self):


        #solicita la edad minima y maxima para filtrar
        edad_min = simpledialog.askinteger("Filtrar Encuestas", "Edad minima:")
        edad_max = simpledialog.askinteger("Filtrar Encuestas", "Edad maxima:")
        if edad_min is not None and edad_max is not None:
            encuestas = self.encuestas.leer()
            encuestas_filtradas =[e for e in encuestas if edad_min <=e[1] <= edad_max]


            encuestas_texto = "\n".join(map(str,encuestas_filtradas))
            messagebox.showinfo("Encuestas Filtradas", encuestas_texto)
        else:
            messagebox.showwarning("CUIDADO","No has introducido valores validos para el filtro")

Permite filtrar las encuestas dentro de un rango de edad

Ejecución de la interfaz
if __name__ == "__main__":
    ventana = tk.Tk()
    As = AlcoholSalud(ventana)
    ventana.mainloop()



tk.Tk(): Crea la ventana principal de la interfaz gráfica.
ventana.mainloop(): Inicia el bucle de la interfaz, manteniendo la ventana abierta y lista para las interacciones del usuario.

Parte de conexión a la base de datos
Métodos
    def __init__(self):
        self.conn = None

Este es el método constructor de la clase. Define un atributo self.conn, que se inicializa como None y se usará para almacenar la conexión con la base de datos.

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
   

host="localhost": Esto indica que el servidor de base de datos se encuentra en la misma máquina.
user="root" y password="campusfp": Aquí se especifican el nombre de usuario y la contraseña para acceder a la base de datos.
database="ENCUESTAS": Se establece la conexión con la base de datos denominada ENCUESTAS.
return self.conn: Si la conexión se realiza con éxito, este método devuelve el objeto self.conn, que representa la conexión activa.

Bloque try-except: En caso de que ocurra un error durante la conexión, como que la base de datos no esté disponible o que las credenciales sean incorrectas, se captura el error y se muestra un mensaje que indica el problema.

    def cerrar_conexion(self):
        if self.conn.is_connected():


            self.conn.close()
            print("Conexion cerrada")



self.conn.is_connected(): Comprueba si la conexión (self.conn) está activa en este momento.
self.conn.close(): Si la conexión está activa, la cierra para liberar los recursos utilizados.
print("Conexión cerrada"): Imprime un mensaje que indica que la conexión se ha cerrado correctamente. 

Operaciones CRUD
Operación crear
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

función: Este método agrega una nueva encuesta a la base de datos.
Proceso:
Establece una conexión con la base de datos (self.conn) y crea un cursor para ejecutar la consulta SQL.
Define la consulta SQL INSERT INTO encuesta VALUES (%s, ...), utilizando marcadores de posición (%s) para insertar datos de manera dinámica.
Utiliza cursor.execute(query, values) para ejecutar la consulta con los valores proporcionados.
Emplea self.conn.commit() para confirmar los cambios en la base de datos.
Resultado: Si se ejecuta correctamente, imprime "Encuesta agregada"; de lo contrario, muestra un mensaje de error.

Operación leer
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
   

Función: Este método recupera todas las encuestas almacenadas en la base de datos.
Proceso:
Crea un cursor y define la consulta SQL SELECT * FROM encuesta para obtener todos los registros de la tabla encuesta.
Ejecuta la consulta con cursor.execute(query) y utiliza cursor.fetchall() para obtener todos los resultados.
Devuelve el resultado como una lista de registros.
Resultado: Retorna todas las encuestas, o imprime un mensaje de error si ocurre un fallo.


Operación actualizar
#metodo para actualizar una encuesta en la base de datos
    def actualizar(self, idEncuesta, columna, valor_actualizado):
        try:
            cursor = self.conn.cursor()
            query = f"UPDATE encuesta SET {columna} = %s WHERE idEncuesta = %s"
            values = (valor_actualizado, idEncuesta)
            cursor.execute(query,values)
            self.conn.commit()
            print("Encuesta actualizada")
        except mysql.connector.Error as error:
            print(f"No se pudo leer las encuestas: {error}")

Función: Este método modifica una columna específica de una encuesta, utilizando el idEncuesta.
Proceso:
Define la consulta SQL UPDATE encuesta SET {columna} = %s WHERE idEncuesta = %s, donde {columna} es el campo que se desea actualizar.
Utiliza cursor.execute(query, values) para ejecutar la consulta con el nuevo valor y el idEncuesta indicado.
Emplea self.conn.commit() para guardar los cambios.
Resultado: Muestra "Encuesta actualizada" si se realiza con éxito, o un mensaje de error en caso contrario.

Operacion eliminar
#metodo para eliminar una  encuesta en la base de datos
    def eliminar(self,idEncuesta):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM encuesta WHERE idEncuesta = %s"
            values = (idEncuesta)
            cursor.execute(query,values)
            self.conn.commit()
            print("Encuesta eliminada")
        except mysql.connector.Error as error:
            print(f"No se pudo leer las encuestas: {error}")

Función: Este método se encarga de eliminar una encuesta específica de la base de datos utilizando el idEncuesta.
Proceso:
Se define la consulta SQL DELETE FROM encuesta WHERE idEncuesta = %s para eliminar el registro correspondiente.
Se ejecuta la consulta y se confirma el cambio en la base de datos con self.conn.commit().
Resultado: Se imprime "Encuesta eliminada" si la operación es exitosa, o un mensaje de error en caso de que falle.

Exportación a Excel

La función comienza llamando al método leer() de la clase encuestas, que se encarga de obtener todas las encuestas que están almacenadas en la base de datos. Este método devuelve los datos en forma de una lista de tuplas, donde cada tupla representa una encuesta.
      encuestas = self.encuestas.leer()

Aquí se define la lista de columnas, que incluye los nombres de las columnas correspondientes a cada campo en la base de datos. Estos nombres se utilizarán en la exportación para generar las etiquetas de encabezado en el archivo de Excel.

 columnas = ["ID","Edad","Sexo", "Bebidas por semana","Cervezas por semana","Bebidas Fin de semana"
                    "Bebidas destiladas","Vinos por semana","Perdidas de control","Diversion vs dependencia","Problemas digestivos","Tension alta","Dolor de cabeza","Nueva columna"]

La biblioteca pandas se utiliza para transformar los datos de las encuestas en un DataFrame, que es una estructura de datos de pandas perfecta para manejar tablas de datos. Se asignan los nombres de las columnas que se definieron previamente.
 df = pd.DataFrame(encuestas,columns=columnas)

El método to_excel() de pandas permite exportar un DataFrame a un archivo de Excel llamado encuestas.xlsx. Al usar el parámetro index=False, se asegura que el índice del DataFrame no se incluya en el archivo, exportando únicamente los datos de las encuestas.
df.to_excel("encuestas.xlsx", index=False)

Al finalizar la exportación, la función presenta un cuadro de mensaje (messagebox.showinfo) para notificar al usuario que los datos se han exportado correctamente.
messagebox.showinfo("Exito","Datos exportados exitosamenre")









Visualización de datos en gráficos


La función inicia llamando al método leer() de la clase encuestas, que recupera todas las encuestas guardadas en la base de datos. A continuación, se extraen dos tipos de datos clave para el gráfico:

Edades (edades): estos datos se obtienen de cada encuesta y reflejan la edad de cada encuestado.

Cantidad de Bebidas por Semana (bebidas): también se extraen de las encuestas y representan el número de bebidas alcohólicas que cada encuestado consume a la semana.
encuestas = self.encuestas.leer()
        #coge las edades y la scantidades de bebidas por semana
        edades = [encuesta[1] for encuesta in encuestas]
        bebidas = [encuesta[3] for encuesta in encuestas]

Con matplotlib, se crea un gráfico de barras que muestra lo siguiente:

El eje X indica las edades de los encuestados.
El eje Y muestra la cantidad de bebidas consumidas cada semana.
Este tipo de gráfico es perfecto para comparar cantidades en diferentes categorías, en este caso, el consumo semanal de alcohol entre varios grupos de edad.
plt.bar(edades,bebidas)

Las etiquetas y el título del gráfico facilitan a los usuarios la interpretación de la visualización:

Etiqueta del Eje X: 'Edad' – Señala que el eje horizontal representa las edades de los encuestados.
Etiqueta del Eje Y: 'Bebidas por semana' – Indica la cantidad de bebidas consumidas semanalmente en el eje vertical.
Título: 'Consumo de alcohol por edad' – Explica el objetivo del gráfico.

plt.xlabel('Edad')
        plt.ylabel('Bebidas por semana')
        plt.title('Consumo de alcohol por edad')
        plt.show()

