from almacenamiento import guardar_datos

def añadir_trainer(datos, nombre, especialidad, telefono):
    nuevo_id = 1 if not datos["trainers"] else max(t["id"] for t in datos["trainers"]) + 1
    trainer = {
        "id" : nuevo_id,
        "nombre" : nombre,
        "especialidad" : especialidad,
        "telefono" : telefono,
        "estado" : "Activo",
        "campers_asignados": []  
    }
    datos["trainers"].append(trainer)
    guardar_datos(datos)
    return trainer

def ver_trainers(datos):
    if not datos["trainers"]:
        print("No hay trainers activos.")
        return
    print("\n--- Listado de trainers ---")
    for t in datos["trainers"]:
        print(f"ID: {t['id']} | Nombre: {t['nombre']} | Estado: {t['estado']} | Teléfono: {t['telefono']}")

def actualizar_trainer(datos, id_trainer, nombre=None, especialidad = None, telefono = None, estado = None):
    for t in datos["trainers"]:
        if t["id"] == id_trainer :
            if nombre is not None:
                t["nombre"] = nombre
            if especialidad is not None:
                t["especialidad"] = especialidad
            if telefono is not None:
                t["telefono"] = telefono
            if estado is not None:
                t["estado"] = estado
            guardar_datos(datos)
            return True
    return False

def eliminar_trainer(datos, id_trainer):
    if not datos["trainers"]:
        print("No hay trainers activos, no se puede eliminar.")
        return
    for t in datos["trainers"]:
        if t["id"] == id_trainer:
            datos["trainers"].remove(t)
            guardar_datos(datos)
            print("Trainer eliminado con éxito.")
            return True
    print("No se encontró un trainer con ese ID.")  
    return False
