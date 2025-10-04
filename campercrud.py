from almacenamiento import guardar_datos

def actualizar_estado_por_nota_inicial(camper):
    nota = camper["nota"]
    if nota >= 60:
        camper["estado"] = "Aprobado"
        camper["riesgo"] = "N/A" 
    else:
        camper["estado"] = "Inscrito" 
        camper["riesgo"] = "N/A"

def crear_camper(datos, nombre, apellidos, direccion, acudiente, edad, ruta, celular, fijo):
    nuevo_id = 1 if not datos["campers"] else max(c["id"] for c in datos["campers"]) + 1
    camper = {
        "id": nuevo_id,
        "nombres": nombre,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "edad": edad,
        "ruta": ruta,
        "celular": celular,
        "fijo": fijo,
        "riesgo": None,
        "nota": 0,             
        "estado": "Inscrito"   
    }
    datos["campers"].append(camper)
    guardar_datos(datos)
    return camper

def listar_campers(datos):
    campers = datos.get("campers", [])     
    if not campers:
        print("No hay campers registrados.")
        return        
    print("\n--- Listado de Campers ---")     
    for c in campers:
        print(
            f"ID: {c.get('id', 'N/A')} | Nombre: {c.get('nombres', 'N/A')} | Apellidos: {c.get('apellidos', 'N/A')} | Dirección: {c.get('direccion', 'N/A')} | Acudiente: {c.get('acudiente', 'N/A')} "
            f"\n Edad: {c.get('edad', 'N/A')} | Ruta: {c.get('ruta', 'N/A')} | Celular: {c.get('celular', 'N/A')} | Fijo: {c.get('fijo', 'N/A')} | Nota: {c.get('nota', 0)} | Estado: {c.get('estado', 'N/A')} | Riesgo: {c.get('riesgo', 'N/A')}"
        )

def actualizar_camper(datos, id_camper, nombre=None, apellidos=None, direccion=None, acudiente=None, edad=None, ruta=None, nota=None, celular=None, fijo=None):
    for camper in datos["campers"]:
        if camper["id"] == id_camper:   
            if nombre is not None:
                camper["nombres"] = nombre
            if apellidos is not None:
                camper["apellidos"] = apellidos
            if direccion is not None:
                camper["direccion"] = direccion
            if acudiente is not None:
                camper["acudiente"] = acudiente
            if edad is not None:
                camper["edad"] = edad
            if ruta is not None:
                camper["ruta"] = ruta
            if celular is not None:
                camper["celular"] = celular
            if fijo is not None:
                camper["fijo"] = fijo
            if nota is not None:
                camper["nota"] = nota
            if nota is not None:
                actualizar_estado_por_nota_inicial(camper)                
            guardar_datos(datos)
            return True
    return False

def eliminar_camper(datos, id_camper):
    camper_a_eliminar = None
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            camper_a_eliminar = camper
            break            
    if not camper_a_eliminar:
        print("No se encontró ese camper para eliminar.")
        return False
    id_ruta_asignada = camper_a_eliminar.get("ruta")
    id_trainer_asignado = camper_a_eliminar.get("trainer_asignado")
    if id_ruta_asignada and id_ruta_asignada != "N/A":
        for ruta in datos.get("rutas", []):
            if ruta["id"] == id_ruta_asignada and id_camper in ruta.get("campers_asignados", []):
                ruta["campers_asignados"].remove(id_camper)
                break
    if id_trainer_asignado:
        for trainer in datos.get("trainers", []):
            if trainer["id"] == id_trainer_asignado and id_camper in trainer.get("campers_asignados", []):
                trainer["campers_asignados"].remove(id_camper)
                break
    datos["campers"].remove(camper_a_eliminar)
    guardar_datos(datos)
    return True

def buscar_camper_por_id(datos, id_camper):
    for camper in datos["campers"]:
        if camper["id"] == id_camper:
            return camper
    return None