import os
from almacenamiento import cargar_datos
from menucoordinadorcampers import menu_coordinador_campers
from menucoordinadortrainers import menu_coordinador_trainers
from menucoordinadorrutas import menu_coordinador_rutas
from menucoordinadorevaluaciones import menu_coordinador_evaluaciones
from reportes import menu_reportes 


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_coordinador_principal():
    datos = cargar_datos()
    
    while True:
        clear()
        print("\n--- Menú Principal del Coordinador ---")
        print("1. Gestión de Campers (Inscripción, Actualización)")
        print("2. Gestión de Trainers (CRUD)")
        print("3. Gestión de Rutas y Matrícula")
        print("4. Gestión de Evaluaciones")
        print("5. Módulo de Reportes")
        print("0. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            clear()
            menu_coordinador_campers()
        elif opcion == "2":
            clear()
            menu_coordinador_trainers()
        elif opcion == "3":
            clear()
            menu_coordinador_rutas()
        elif opcion == "4":
            clear()
            menu_coordinador_evaluaciones()
        elif opcion == "5":
            clear()
            menu_reportes(datos) 
        elif opcion == "0":
            print("Cerrando sesión del Coordinador...")
            break
        else:
            print("Opción inválida.")