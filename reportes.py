
from campercrud import buscar_camper_por_id 
from trainercrud import ver_trainers
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def listar_campers_por_estado(datos, estado_buscado):
    campers_filtrados = [c for c in datos["campers"] if c.get("estado") == estado_buscado]
    
    if not campers_filtrados:
        print(f"No hay campers en estado '{estado_buscado}'.")
        return
        
    print(f"\n--- Campers en estado: {estado_buscado} ---")
    for c in campers_filtrados:
        print(f"ID: {c['id']} | Nombre: {c['nombres']} {c['apellidos']} | Ruta: {c.get('ruta', 'N/A')}")
        
    return campers_filtrados 

def listar_campers_bajo_rendimiento(datos):
    campers_riesgo = [
        c for c in datos["campers"] 
        if c.get("estado") == "En riesgo" or (c.get("nota") is not None and c.get("nota") < 60)
    ]
    
    if not campers_riesgo:
        print("No hay campers identificados con riesgo o bajo rendimiento.")
        return
        
    print("\n--- Campers en Rendimiento Bajo / Riesgo ---")
    for c in campers_riesgo:
        print(f"ID: {c['id']} | Nombre: {c['nombres']} {c['apellidos']} | Estado: {c['estado']} | Nota Inicial: {c.get('nota', 'N/A')}")

def listar_asociados_por_ruta(datos):
    from rutascrud import listar_rutas

    listar_rutas(datos)
    try:
        id_ruta = int(input("Ingrese el ID de la ruta a consultar: "))
    except ValueError:
        print("ID de ruta inválido.")
        return      
    ruta_encontrada = next((r for r in datos["rutas"] if r["id"] == id_ruta), None)   
    if not ruta_encontrada:
        print("Ruta no encontrada.")
        return
    print(f"\n--- Asociados a Ruta: {ruta_encontrada['nombre']} ---")
    trainer_id = ruta_encontrada.get("trainer_asignado")
    if trainer_id:
        trainer = next((t for t in datos["trainers"] if t["id"] == trainer_id), None)
        print(f"Trainer Asignado: {trainer['nombre'] if trainer else 'ID no encontrado'}")
    else:
        print("Trainer Asignado: N/A")
    campers_asignados_ids = ruta_encontrada.get("campers_asignados", [])
    if campers_asignados_ids:
        print("\nCampers Asignados:")
        for camper_id in campers_asignados_ids:
            camper = buscar_camper_por_id(datos, camper_id)
            if camper:
                print(f"  - ID: {camper['id']} | Nombre: {camper['nombres']} {camper['apellidos']} | Estado: {camper['estado']}")
    else:
        print("No hay campers asignados a esta ruta.")


def reporte_aprobados_reprobados_por_modulo(datos): 
    if not datos.get("rutas"):
        print("No hay rutas registradas para generar el reporte modular.")
        return
    print("\n--- Reporte Modular de Aprobación ---")   
    for ruta in datos["rutas"]:
        print(f"\nRuta ID {ruta['id']}: {ruta['nombre']}")
        modulos = ruta.get("modulos", [])
        resultados_modulos = {mod: {"Aprobados": 0, "Reprobados": 0} for mod in modulos}        
        campers_en_ruta = [
            buscar_camper_por_id(datos, cid) 
            for cid in ruta.get("campers_asignados", [])
        ]
        for camper in campers_en_ruta:
            if camper and camper.get("evaluaciones"):
                evaluaciones_ruta = camper["evaluaciones"].get(str(ruta['id']), {})                
                for modulo_nombre in modulos:
                    eval_modulo = evaluaciones_ruta.get(modulo_nombre.strip(), {}) 
                    
                    if eval_modulo:
                        if eval_modulo.get("aprobado"):
                            resultados_modulos[modulo_nombre.strip()]["Aprobados"] += 1
                        else:
                            resultados_modulos[modulo_nombre.strip()]["Reprobados"] += 1

        for modulo, resultados in resultados_modulos.items():
            total = resultados["Aprobados"] + resultados["Reprobados"]
            if total > 0:
                print(f"  Módulo '{modulo}': Total Evaluados: {total}")
                print(f"    - Aprobados: {resultados['Aprobados']}")
                print(f"    - Reprobados: {resultados['Reprobados']}")
            else:
                print(f" Módulo '{modulo}': Sin evaluaciones registradas.")



def menu_reportes(datos):
    from campercrud import listar_campers 
    from trainercrud import ver_trainers 

    while True:
        clear()
        print("\n--- Módulo de Reportes ---")
        print("1. Listar campers en estado 'Inscrito'")
        print("2. Listar campers en estado 'Aprobado' (Examen Inicial)")
        print("3. Listar Trainers activos")
        print("4. Listar campers con Bajo Rendimiento / Riesgo")
        print("5. Listar Campers y Trainers asociados a una Ruta")
        print("6. Reporte de Aprobados/Reprobados por Módulo/Ruta")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear()
            listar_campers_por_estado(datos, "Inscrito")
            input("Presione enter para continuar...")
        elif opcion == "2":
            clear()
            listar_campers_por_estado(datos, "Aprobado")
            input("Presione enter para continuar...")
        elif opcion == "3":
            clear()
            ver_trainers(datos)
            input("Presione enter para continuar")
        elif opcion == "4":
            clear()
            listar_campers_bajo_rendimiento(datos)
            input("Presione enter para continuar...")
        elif opcion == "5":
            clear()
            listar_asociados_por_ruta(datos)
            input("Presione enter para continuar...")
        elif opcion == "6":
            clear()
            reporte_aprobados_reprobados_por_modulo(datos)
            input("Presione enter para continuar")
        elif opcion == "0":
            clear()
            print("Saliendo del menú...")
            break
        else:
            print("Opción no válida.")