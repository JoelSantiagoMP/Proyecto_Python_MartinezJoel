from almacenamiento import guardar_datos

def calcular_nota_final(nota_teo, nota_prac, nota_quiz):
    return round(nota_teo * 0.3 + nota_prac * 0.6 + nota_quiz * 0.1, 2)

def registrar_evaluacion(datos, id_camper, id_ruta, id_modulo, nota_teo, nota_prac, nota_quiz):
    nota_final = calcular_nota_final(nota_teo, nota_prac, nota_quiz)
    
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            if "evaluaciones" not in camper:
                camper["evaluaciones"] = {}
            if id_ruta not in camper["evaluaciones"]:
                camper["evaluaciones"][id_ruta] = {}
            camper["evaluaciones"][id_ruta][id_modulo] = {
                "teorica": nota_teo,
                "practica": nota_prac,
                "quiz": nota_quiz,
                "final": nota_final,
                "aprobado": nota_final >= 60
            }
            if nota_final < 60:
                camper["riesgo"] = "Rendimiento Bajo" 
                print(f"Alerta: Camper {camper['nombres']} tiene Rendimiento Bajo en el módulo {id_modulo}.")
            elif camper.get("riesgo") == "Rendimiento Bajo":
                camper["riesgo"] = "N/A"            
            guardar_datos(datos)
            return True
    
    return False

def listar_riesgo_alto(datos):
    riesgos = [
        c for c in datos["campers"] 
        if c.get("estado") in ["En riesgo", "Reprobado"] or 
           c.get("riesgo") == "Rendimiento Bajo" 
    ]    
    if not riesgos:
        print("No hay campers en riesgo alto")
        return        
    print("\n--- Campers en riesgo alto ---")
    for c in riesgos:
        riesgo_actual = c.get("riesgo", c.get("estado")) 
        print(f"ID: {c['id']} | Nombre: {c['nombres']} | Estado General: {c['estado']} | Riesgo Modular: {riesgo_actual}")

def ver_evaluaciones_camper(datos, id_camper):
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            if "evaluaciones" not in camper or not camper["evaluaciones"]:
                print(f"El camper {camper['nombres']} {camper['apellidos']} no tiene evaluaciones registradas.")
                return
            print(f"\nEvaluaciones de {camper['nombres']} {camper['apellidos']}:")
            for ruta_id, modulos in camper["evaluaciones"].items():
                print(f"Ruta ID {ruta_id}:")
                for mod_id, notas in modulos.items():
                    print(f"  Módulo {mod_id} → Teo: {notas['teorica']}, Prac: {notas['practica']}, Quiz: {notas['quiz']}, Final: {notas['final']}, Aprobado: {notas['aprobado']}")
            return
    print("Camper no encontrado")
