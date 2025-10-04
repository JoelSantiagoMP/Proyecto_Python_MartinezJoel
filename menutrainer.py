from almacenamiento import guardar_datos, cargar_datos 
from opcionestrainer import editar_notas, colocar_reporte, ver_info_trainer, ver_campers_asignados
import os 

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_trainer(trainer, datos):
    if not trainer:
        print("No se pudo iniciar sesión en el menú trainer.")
        return
    trainer_id = trainer["id"]
    
    while True:
        datos = cargar_datos()
        current_trainer = next((t for t in datos.get("trainers", []) if t["id"] == trainer_id), None)
        
        if not current_trainer:
             print("Su perfil de trainer ya no existe en la base de datos. Cerrando sesión.")
             break
        
        clear()
        print(f"\n--- Menú del trainer {current_trainer['nombre']} ---")
        print("1. Ver mi información")
        print("2. Ver campers asignados")
        print("3. Editar notas de campers")
        print("4. Generar reporte a un camper")
        print("5. Cerrar sesión")
        
        opcion = input("Seleccione una opcion: ")       
        if opcion == "1":
            ver_info_trainer(current_trainer)
        elif opcion == "2":
            ver_campers_asignados(current_trainer, datos)
        elif opcion =="3":
            editar_notas(datos, current_trainer) 
        elif opcion == "4":
            colocar_reporte(datos, current_trainer) 
        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
        
        input("Presione Enter para continuar...")