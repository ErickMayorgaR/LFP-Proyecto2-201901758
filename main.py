from tkinter import filedialog
from tkinter import *
from CargarArchivo import *


#ir_seleccion = ArchivoCarga()


def cargar_archivo():

   # ruta = Tk()
    #ruta.filename = filedialog.askopenfilename(filetypes=(("txt files", "*.lfp"), ("all files", "*.*")))

    #file = open(ruta.filename, "r", encoding='utf-8')
    file = open('C:/Users/Erick Mayorga/Desktop/LFP Proyecto2-201901758/-LFP-Proyecto2_Archivos-main/lista.lfp','r', encoding='utf-8')
    #print(file)
    #ruta.destroy()
    info = file.read()
    ir_seleccion = ArchivoCarga()
    ir_seleccion.analisis(info)

def generar_graficas():
    print("algo")
    #ir_seleccion.mejorRuta()


def salir():
    sys.exit(0)

def opciones():
    print("\n")
    print("Proyecto2 LFP Erick Ivan Mayorga Rodriguez 201901758")
    print("Seleccione una Opcion")
    print("1.Cargar Archivo ")
    print("2.Generar Grafico")
    print("3.Salir")


def main_menu():
    opcion = -1
    while opcion != 4:
        opciones()
        opcion = int(input())
        if opcion == 1:
            cargar_archivo()
        if opcion == 2:
            generar_graficas()
        if opcion == 3:
            salir()
        else:
            print("Algo")


main_menu()
"""def separador():
    print("algo") """
