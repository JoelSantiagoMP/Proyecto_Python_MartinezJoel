from almacenamiento import cargar_datos
from campercrud import crear_camper, listar_campers, actualizar_camper, eliminar_camper
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu_coordinador_campers():
    
    while True:
        datos = cargar_datos()
        clear()
        print("\n--- Menú Coordinador de Campers ---")
        print("1. Crear camper (Inscripción)")
        print("2. Listar campers")
        print("3. Actualizar camper")
        print("4. Eliminar camper")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            clear()
            try:
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ") 
                direccion = input("Dirección: ")
                acudiente = input("Acudiente: ")
                celular = input("Celular: ")
                fijo = input("Fijo: ")
                edad = int(input("Edad: "))
                while edad < 0:
                    print("La edad no puede ser negativa.")
                    edad = int(input("Edad: "))
                ruta = "N/A" 
                crear_camper(datos, nombre, apellidos, direccion, acudiente, edad, ruta, celular, fijo)
                print("Camper creado con éxito y en estado 'Inscrito'")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar la edad como número.")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            clear()
            listar_campers(datos)
            input("Presione Enter para continuar...")

        elif opcion == "3":
            clear()
            listar_campers(datos)
            try:
                id_c = int(input("ID del camper a actualizar: "))
                
                print("Deje en blanco lo que no quiera cambiar. Para nota, ingrese el valor (0-100).")
                
                nuevo_nombre = input("Nuevo nombre: ") or None
                nuevos_apellidos = input("Nuevos apellidos: ") or None
                nueva_direccion = input("Nueva dirección: ") or None
                nuevo_acudiente = input("Nuevo acudiente: ") or None
                nuevo_celular = input("Nuevo celular: ") or None
                nuevo_fijo = input("Nuevo fijo: ") or None
                nueva_edad_input = input("Nueva edad: ")
                nueva_ruta = input("Nueva ruta (N/A si no aplica): ") or None
                
                nueva_edad = int(nueva_edad_input) if nueva_edad_input else None
                
                nueva_nota_input = input("Nueva Nota de EXAMEN INICIAL (0-100): ")
                
                nueva_nota = None
                if nueva_nota_input:
                    try:
                        nueva_nota = float(nueva_nota_input)
                        if not 0 <= nueva_nota <= 100:
                             print("Valor de nota INICIAL inválido. Debe ser entre 0 y 100. Se omite la actualización de nota.")
                             nueva_nota = None
                    except ValueError:
                        print("Valor de nota inválido. Se omite.")
                        nueva_nota = None              
                        
                if actualizar_camper(datos, id_c, 
                                     nombre=nuevo_nombre, 
                                     apellidos=nuevos_apellidos, 
                                     direccion=nueva_direccion,
                                     acudiente=nuevo_acudiente,
                                     celular=nuevo_celular, 
                                     fijo=nuevo_fijo, 
                                     edad=nueva_edad, 
                                     ruta=nueva_ruta, 
                                     nota=nueva_nota):
                    print("Camper actualizado con éxito. El estado fue re-evaluado.")
                else:
                    print("No se encontró el camper")
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar un ID y la edad (si se cambia) como números.")
            
            input("Presione Enter para volver al menú...")

        elif opcion == "4":
            clear()
            listar_campers(datos)
            try:
                id_c = int(input("ID del camper a eliminar: "))
                if eliminar_camper(datos, id_c):
                    print("Camper eliminado")
                else:
                    print("No se encontró ese camper")
            except ValueError:
                print("Entrada inválida")
            input("Presione Enter para continuar...")

        elif opcion == "0":
            clear()
            print("Saliendo al menú principal del Coordinador...")
            break
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")
