import tkinter as tk #libreria para crear interfaces graficas
import matplotlib.pyplot as plt #Libreria para generar graficos
import pandas as pd #Libreria para trabajar con datos y exportarlos a excel
#Importaciones de los modulos restantes de tkinter
from tkinter import simpledialog #crear cuadros de entraadas simples
from tkinter import messagebox # para cuadros de mensajes emergentes
from CRUD import EEncuestas
from conexionBD import CConexion


class AlcoholSalud:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Encuesta de salud y consumo de alcohol")

        self.bd = CConexion()
        self.bd.connectionBD()
        if self.bd.conn:

            self.encuestas = EEncuestas(self.bd.conn)
        
        else:("No se puede conectar a la base de datos")

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

#metodo para agregar una nueva encuesta
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

    #metodo para ver visualmente los datos de la base de datos
    def ver_encuesta(self):
        encuestas = self.encuestas.leer()
        #convierte las encuestas en candenas de texto
        encuestas_texto = "\n".join(map(str,encuestas))
        #muestra las encuestas en un cuadro de mensaje
        messagebox.showinfo("Encuestas", encuestas_texto)


    #metodo para actualizar la encuesta
    def actualizar_encuesta(self):

        #pide el id, la columna a actualizar y el nuevo valor 
        idEncuesta = simpledialog.askinteger("Actualizar Encuesta", "ID de la encuesta a actualizar:")
        columna =simpledialog.askstring("Actualiar encuesta", "Columna a actualizar(Por ejemplo: edad):")
        valor_actualizado = simpledialog.askinteger("Actualizar encuesta", "Nuevo valor:")

    #Llama al metodo actualizar de EEncuestas
        self.encuestas.actualizar(idEncuesta,columna,valor_actualizado)
        messagebox.showinfo("Exito", "Encuesta actualizada exitosamente")
    
    #metodo para eliminar una encuesta dando el ID
    def eliminar_encuesta(self):
        idEncuesta = simpledialog.askinteger("Eliminar Encuesta", "ID de la encuesta a eliminar:")
        #Llama al metodo eliminar de EEncuestas
        self.encuestas.eliminar(idEncuesta)
        messagebox.showinfo("Exito", "Encuesta eliminada exitosamente")
    
    #metodo generar grafico de barras
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
    
    #metodo para exportar la base de datos a excel 
    def exportar_excel(self):
        #obtiene las encuestas y define los nombres de las columnas
        encuestas = self.encuestas.leer()
        columnas = ["ID","Edad","Sexo", "Bebidas por semana","Cervezas por semana","Bebidas Fin de semana"
                    "Bebidas destiladas","Vinos por semana","Perdidas de control","Diversion vs dependencia","Problemas digestivos","Tension alta","Dolor de cabeza","Nueva columna"]
        df = pd.DataFrame(encuestas,columns=columnas)
        df.to_excel("encuestas.xlsx", index=False)
        messagebox.showinfo("Exito","Datos exportados exitosamenre")
    
    #metodo para filtrar las encuestas por edad
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


if __name__ == "__main__":
    ventana = tk.Tk()
    As = AlcoholSalud(ventana)
    ventana.mainloop()



