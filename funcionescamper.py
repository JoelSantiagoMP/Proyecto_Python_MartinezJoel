def camper_login(datos):
    if not datos.get("campers"):
        print("No hay campers registrados. ")
        return None
    while True:
        try:
            entrada = input("Ingrese su ID de camper (o escriba 'salir' para volver): ")
            if entrada.lower() == "salir":
                return None
            id_camper = int(entrada)
            for camper in datos["campers"]:
                if camper["id"] == id_camper:
                    nombre = input("Ingrese su nombre para confirmar: ")
                    if nombre.lower() == camper["nombres"].lower():
                        print(f"Bienvenido {camper['nombres']} {camper['apellidos']}")
                        return camper
                    else:
                        print("Nombre incorrecto.")
                        break
            else:
                print("ID no encontrado.")
        except ValueError:
            print("Dato inválido.")

def ver_mi_informacion_camper(camper):
    print("\n--- Información del camper ---")
    print(f"ID: {camper['id']}")
    print(f"Nombre: {camper['nombres']}")
    print(f"Apellidos: {camper['apellidos']}")
    print(f"Direccion: {camper['direccion']}")
    print(f"Acudiente: {camper['acudiente']}")
    print(f"Edad: {camper['edad']}")
    print(f"Ruta: {camper.get('ruta', 'No asignada')}")
    print(f"Estado: {camper.get('estado', 'Sin estado')}")
    print(f"Nota: {camper.get('nota', 'Sin nota')}")

def ver_reportes_camper(camper):
    reportes = camper.get("reportes", [])
    if not reportes:
        print("No tienes reportes.")
    else:
        print("\n--- Reportes ---")
        for i, r in enumerate(reportes,1):
            print(f"{i}. {r}")

def ver_estado_academico(camper):
    nota = camper.get("nota", None)
    if nota is None:
        print("Aún no tienes notas registradas.")
    else:
        if nota<60:
            print(f"Tu nota es {nota} | Estado: En riesgo")
        else:
            print(f"Tu nota es {nota} | Estado: Aprobado")