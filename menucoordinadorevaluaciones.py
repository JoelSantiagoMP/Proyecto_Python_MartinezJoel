from evaluacioncrud import listar_riesgo_alto, ver_evaluaciones_camper
from almacenamiento import cargar_datos
from campercrud import listar_campers
from rutascrud import listar_rutas
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_coordinador_evaluaciones():
    while True:
        datos = cargar_datos()
        clear()         
        print("\n--- Menú Coordinador de Evaluaciones ---")
        print("1. Ver evaluaciones de un camper") 
        print("2. Listar campers en riesgo alto") 
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            clear() 
            listar_campers(datos)
            try:
                id_camper = int(input("ID del camper a ver evaluaciones: "))
                ver_evaluaciones_camper(datos, id_camper)
            except ValueError:
                print("Entrada inválida. Debe ingresar un ID numérico.")
            input("Presione Enter para volver al menú...")
        
        elif opcion == "2":
            clear()
            listar_riesgo_alto(datos)
            input("Presione Enter para volver al menú...")
        
        elif opcion == "0":
            clear()
            print("Saliendo del menú de evaluaciones...")
            break
        
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")