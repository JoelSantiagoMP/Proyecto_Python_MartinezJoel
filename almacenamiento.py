import json

ARCHIVO = "data.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"campers": [], "trainers": [], "rutas": []}
    except json.JSONDecodeError:
        return {"campers": [], "trainers": [], "rutas": []}

def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)
