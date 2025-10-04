from almacenamiento import guardar_datos    
from campercrud import buscar_camper_por_id
def crear_ruta(datos, nombre, modulos, sgdb_principal, sgdb_alternativo, capacidad=33):
    nuevo_id = 1 if not datos["rutas"] else max(r["id"] for r in datos["rutas"]) + 1
    ruta = {
        "id": nuevo_id,
        "nombre": nombre,
        "modulos": modulos, 
        "sgdb_principal": sgdb_principal,
        "sgdb_alternativo": sgdb_alternativo,
        "capacidad": capacidad,
        "campers_asignados": []
    }
    datos["rutas"].append(ruta)
    guardar_datos(datos)
    return ruta

def listar_rutas(datos):
    if not datos["rutas"]:
        print("No hay rutas registradas.")
        return
    print("\n--- Listado de Rutas ---")
    for r in datos["rutas"]:
        print(f"ID: {r['id']} | Nombre: {r['nombre']} | Capacidad: {r['capacidad']} | Campers asignados: {len(r['campers_asignados'])}")
        print(f"  Módulos: {', '.join(r['modulos'])}")
        print(f"  SGDB Principal: {r['sgdb_principal']} | SGDB Alternativo: {r['sgdb_alternativo']}")
        print("-" * 50)

def actualizar_ruta(datos, id_ruta, nombre=None, modulos=None, sgdb_principal=None, sgdb_alternativo=None, capacidad=None):
    for r in datos["rutas"]:
        if r["id"] == id_ruta:
            if nombre is not None:
                r["nombre"] = nombre
            if modulos is not None:
                r["modulos"] = modulos
            if sgdb_principal is not None:
                r["sgdb_principal"] = sgdb_principal
            if sgdb_alternativo is not None:
                r["sgdb_alternativo"] = sgdb_alternativo
            if capacidad is not None:
                r["capacidad"] = capacidad
            guardar_datos(datos)
            return True
    return False

def eliminar_ruta(datos, id_ruta):
    for r in datos["rutas"]:
        if r["id"] == id_ruta:
            if r["campers_asignados"]:
                print("No se puede eliminar una ruta con campers asignados.")
                return False
            datos["rutas"].remove(r)
            guardar_datos(datos)
            return True
    return False

def remover_camper_de_ruta(datos, id_ruta, id_camper):
    for r in datos["rutas"]:
        if r["id"] == id_ruta:
            if id_camper in r["campers_asignados"]:
                r["campers_asignados"].remove(id_camper)
                guardar_datos(datos)
                return True
            else:
                print("Camper no está asignado a esta ruta.")
                return False
    print("Ruta no encontrada.")
    return False

def asignar_camper_a_ruta(datos, id_ruta, id_camper):
    ruta_obj = next((r for r in datos["rutas"] if r["id"] == id_ruta), None)
    
    if not ruta_obj:
        print("Error: Ruta no encontrada para la asignación.")
        return False
        
    capacidad = ruta_obj.get("capacidad", 33) 
    campers_actuales = len(ruta_obj.get("campers_asignados", []))
    
    if campers_actuales >= capacidad:
        print(f"Error: La ruta '{ruta_obj['nombre']}' ha alcanzado su capacidad máxima ({capacidad}).")
        return False
        
    if id_camper not in ruta_obj.get("campers_asignados", []):
        ruta_obj["campers_asignados"].append(id_camper)
        return True
    return True 

def matricular_camper(datos, id_camper, id_ruta, id_trainer, salon, fecha_inicio, fecha_fin):
    camper = next((c for c in datos["campers"] if c["id"] == id_camper), None)
    ruta_obj = next((r for r in datos["rutas"] if r["id"] == id_ruta), None)
    trainer_obj = next((t for t in datos["trainers"] if t["id"] == id_trainer), None)
    if not camper:
        print("Error: Camper no encontrado.")
        return False
    if not ruta_obj:
        print("Error: Ruta no encontrada.")
        return False
    if not trainer_obj:
        print("Error: Trainer no encontrado.")
        return False
    
    if camper.get("estado") != "Aprobado":
        print(f"Error: El camper {camper['nombres']} no está en estado 'Aprobado'. Estado actual: {camper.get('estado')}.")
        return False
    if not asignar_camper_a_ruta(datos, id_ruta, id_camper):
        return False 
    if "trainers_asignados" not in ruta_obj:
        ruta_obj["trainers_asignados"] = []
    if id_trainer not in ruta_obj["trainers_asignados"]:
        ruta_obj["trainers_asignados"].append(id_trainer)
    if "campers_asignados" not in trainer_obj:
        trainer_obj["campers_asignados"] = []         
    if id_camper not in trainer_obj["campers_asignados"]:
        trainer_obj["campers_asignados"].append(id_camper)
    camper["ruta"] = id_ruta
    camper["estado"] = "Cursando" 
    camper["trainer_asignado"] = id_trainer
    camper["matricula"] = {
        "ruta_id": id_ruta,
        "trainer_id": id_trainer,
        "salon": salon,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin
    }
    guardar_datos(datos)
    print(f"Matrícula exitosa. Camper {camper['nombres']} asignado a Ruta {ruta_obj['nombre']} y Trainer {trainer_obj['nombre']}.")
    return True

def remover_camper_de_ruta(datos, id_ruta, id_camper):
    ruta_obj = next((r for r in datos["rutas"] if r.get("id") == id_ruta), None)
    camper_obj = next((c for c in datos["campers"] if c.get("id") == id_camper), None)
    
    if not ruta_obj:
        print("Error: Ruta no encontrada.")
        return False
    if not camper_obj:
        print("Error: Camper no encontrado.")
        return False
    if id_camper in ruta_obj.get("campers_asignados", []):
        ruta_obj["campers_asignados"].remove(id_camper)
    else:
        print(f"Advertencia: El Camper ID {id_camper} no estaba asignado a la Ruta ID {id_ruta}.")
    id_trainer = camper_obj.get("trainer_asignado")
    if id_trainer:
        trainer_obj = next((t for t in datos["trainers"] if t.get("id") == id_trainer), None)
        if trainer_obj and id_camper in trainer_obj.get("campers_asignados", []):
            trainer_obj["campers_asignados"].remove(id_camper)
    camper_obj["ruta"] = "N/A"
    camper_obj["trainer_asignado"] = None
    if camper_obj.get("nota") is not None and camper_obj.get("nota") >= 60:
        camper_obj["estado"] = "Aprobado" 
    else:
        camper_obj["estado"] = "Inscrito" 
        
    camper_obj.pop("matricula", None) 

    guardar_datos(datos)
    print(f"Camper {camper_obj['nombres']} removido de la Ruta {ruta_obj['nombre']} y desasignado del Trainer.")
    return True