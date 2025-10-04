from rutascrud import crear_ruta, listar_rutas, actualizar_ruta, eliminar_ruta, asignar_camper_a_ruta, remover_camper_de_ruta, matricular_camper
from almacenamiento import cargar_datos
from campercrud import listar_campers
from trainercrud import ver_trainers
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_coordinador_rutas():
    
    while True:
        clear() 
        datos = cargar_datos() 
        
        print("\n--- Menú Coordinador de Rutas ---")
        print("1. Crear ruta")
        print("2. Listar rutas")
        print("3. Actualizar ruta")
        print("4. Eliminar ruta")
        print("5. Asignar camper a ruta (Pre-matricula)")
        print("6. Remover camper de ruta")
        print("7. Matricular camper aprobado")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            clear()
            nombre = input("Nombre de la ruta: ")
            modulos = input("Módulos separados por coma: ").split(",")
            sgdb_principal = input("SGDB principal: ")
            sgdb_alternativo = input("SGDB alternativo: ")
            capacidad = input("Capacidad máxima (default 33): ")
            capacidad = int(capacidad) if capacidad.isdigit() else 33
            
            crear_ruta(datos, nombre, modulos, sgdb_principal, sgdb_alternativo, capacidad)
            print("Ruta creada con éxito.")
            input("Presione Enter para volver al menú...") 

        elif opcion == "2":
            clear()
            listar_rutas(datos)
            input("Presione Enter para volver al menú...") 

        elif opcion == "3":
            clear()
            listar_rutas(datos)
            try:
                id_r = int(input("ID de la ruta a actualizar: "))
                nombre = input("Nuevo nombre (deje en blanco para no cambiar): ") or None
                modulos_str = input("Nuevos módulos separados por coma (deje en blanco para no cambiar): ")
                modulos = modulos_str.split(",") if modulos_str else None
                sgdb_principal = input("Nuevo SGDB principal: ") or None
                sgdb_alternativo = input("Nuevo SGDB alternativo: ") or None
                capacidad_str = input("Nueva capacidad: ")
                capacidad = int(capacidad_str) if capacidad_str.isdigit() else None
                
                if actualizar_ruta(datos, id_r, nombre, modulos, sgdb_principal, sgdb_alternativo, capacidad):
                    print("Ruta actualizada con éxito.")
                else:
                    print("No se pudo actualizar la ruta.")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar IDs y capacidades numéricas.")
            input("Presione Enter para volver al menú...") 
        elif opcion == "4":
            clear()
            listar_rutas(datos)
            try:
                id_r = int(input("ID de la ruta a eliminar: "))
                if eliminar_ruta(datos, id_r):
                    print("Ruta eliminada con éxito.")
                else:
                    print("No se pudo eliminar la ruta.")
            except ValueError:
                print("Entrada inválida.")
            input("Presione Enter para volver al menú...") 

        elif opcion == "5":
            clear()
            listar_campers(datos)
            listar_rutas(datos)
            try:
                id_camper = int(input("ID del Camper a asignar: "))
                id_ruta = int(input("ID de la Ruta: "))
                if asignar_camper_a_ruta(datos, id_ruta, id_camper):
                    print("Camper asignado a ruta (pre-matrícula) con éxito.")
                else:
                    print("No se pudo asignar el camper a la ruta.")
            except ValueError:
                print("Entrada inválida.")
            input("Presione Enter para volver al menú...") 

        elif opcion == "6":
            clear()
            listar_rutas(datos)
            try:
                id_ruta = int(input("ID de la Ruta: "))
                id_camper = int(input("ID del Camper a remover: "))
                if remover_camper_de_ruta(datos, id_ruta, id_camper):
                    print("Camper removido de la ruta con éxito.")
            except ValueError:
                print("Entrada inválida.")
            input("Presione Enter para volver al menú...")  

        elif opcion == "7":
            clear()
            print("--- Proceso de Matrícula ---")            
            listar_rutas(datos)  
            ver_trainers(datos)            
            try:
                id_camper = int(input("ID del Camper a matricular: "))
                id_ruta = int(input("ID de la Ruta a asignar: "))
                id_trainer = int(input("ID del Trainer responsable: "))
                salon = input("Nombre del Salón/Área: ")
                fecha_inicio = input("Fecha de inicio (DD/MM/AAAA): ")
                fecha_fin = input("Fecha de finalización (DD/MM/AAAA): ")
                matricular_camper(datos, id_camper, id_ruta, id_trainer, salon, fecha_inicio, fecha_fin)

            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar IDs numéricos.")
        
        elif opcion == "0":
            clear()
            print("Saliendo del módulo de gestión de rutas...")
            break
            
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...") 