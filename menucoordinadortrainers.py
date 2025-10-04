from trainercrud import añadir_trainer, eliminar_trainer, actualizar_trainer, ver_trainers
from almacenamiento import cargar_datos
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_coordinador_trainers():
    while True:
        clear() 
        datos = cargar_datos() 
        
        print("\n--- Menú Coordinador de Trainers ---")
        print("1. Añadir trainer")
        print("2. Listar trainers")
        print("3. Actualizar trainers")
        print("4. Eliminar trainer")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            clear()
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            telefono = input("Teléfono: ")
            añadir_trainer(datos, nombre, especialidad, telefono)
            print("Trainer creado con éxito")
            input("Presione Enter para continuar...") 
            
        elif opcion == "2":
            clear()
            ver_trainers(datos)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            clear()
            ver_trainers(datos)
            try:
                id_t = int(input("ID del trainer a actualizar: "))
                print("Deje en blanco lo que no quiera cambiar.")
                nuevo_nombre = input("Nuevo nombre: ") or None
                nueva_especialidad = input("Nueva especialidad: ") or None
                nuevo_telefono = input("Nuevo teléfono: ") or None
                
                if actualizar_trainer(datos, id_t, nuevo_nombre, nueva_especialidad, nuevo_telefono):
                    print("Trainer actualizado con éxito")
                else:
                    print("No se encontró el trainer")
            except ValueError:
                print("Entrada inválida")
            input("Presione Enter para continuar...")

        elif opcion == "4":
            clear()
            ver_trainers(datos)
            try:
                id_t = int(input("ID del trainer a eliminar: "))
                if eliminar_trainer(datos, id_t):
                    print("Trainer eliminado")
                else:
                    print("No se encontró ese trainer")
            except ValueError:
                print("Entrada inválida")
            input("Presione Enter para continuar...") 

        elif opcion == "0":
            clear()
            print("Saliendo del módulo de gestión de trainers...")
            break
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...") 