import os
from almacenamiento import cargar_datos
from funcionescamper import camper_login
from opcionestrainer import trainer_login
from menucamper import menu_camper
from menutrainer import menu_trainer
from menucoordinadorprincipal import menu_coordinador_principal 


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    datos = cargar_datos()
    while True:
        clear()
        print("====================================")
        print("== BIENVENIDO A CAMPUSLANDS APP ==")
        print("====================================")
        print("Seleccione su rol:")
        print("1. Coordinador")
        print("2. Trainer")
        print("3. Camper")
        print("0. Salir del programa")

        rol = input("Ingrese el número de su rol: ")
        datos = cargar_datos() 
        if rol == "1":
            clear()
            menu_coordinador_principal()
        elif rol == "2":
            clear()
            trainer_actual = trainer_login(datos)
            if trainer_actual:
                menu_trainer(trainer_actual, datos)
        elif rol == "3":
            clear()
            camper_actual = camper_login(datos)
            if camper_actual:
                menu_camper(camper_actual)
        elif rol == "0":
            clear()
            print("Gracias por usar CampusLands. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...") 

if __name__ == "__main__":
    main()