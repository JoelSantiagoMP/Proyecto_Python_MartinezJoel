from funcionescamper import ver_estado_academico, ver_mi_informacion_camper, ver_reportes_camper
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_camper(camper):
    if not camper:
        print("No se pudo iniciar sesión en el menú camper.")
        return
    while True:
        clear() 
        print(f"\n--- Menú del camper {camper['nombres']} ---")
        print("1. Ver mi información")
        print("2. Ver mis notas / estado académico")
        print("3. Ver reportes")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            clear()
            ver_mi_informacion_camper(camper)
            input("Pulse enter para continuar...")
        elif opcion == "2":
            clear()
            ver_estado_academico(camper)
            input("Pulse enter para continuar...")
        elif opcion == "3":
            clear()
            ver_reportes_camper(camper)
            input("Pulse enter para continuar...")
        elif opcion == "4":
            clear()
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida, intente nuevamente.")