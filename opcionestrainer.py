from almacenamiento import guardar_datos
from evaluacioncrud import registrar_evaluacion
from campercrud import listar_campers, actualizar_estado_por_nota_inicial

def trainer_login(datos):
    trainers = datos.get("trainers")
    if not trainers:
        print("No hay trainers registrados.")
        return None
    while True:
        try:
            entrada = input("Ingrese su ID de trainer (o escriba 'salir' para volver): ")
            if entrada.lower() == "salir":
                print("Volviendo al menú principal...")
                return None            
            id_trainer = int(entrada)
            trainer_encontrado = next((t for t in trainers if t["id"] == id_trainer), None)
            if trainer_encontrado:
                nombre_ingresado = input(f"ID {id_trainer} encontrado. Ingrese el nombre del trainer para completar la validación: ")                
                if nombre_ingresado.lower() == trainer_encontrado["nombre"].lower():
                    print("Inicio de sesión exitoso.")
                    return trainer_encontrado
                else:
                    print("El nombre no coincide con el ID, intente nuevamente.")
            else:
                print("ID de trainer no encontrado, intente nuevamente.")            
        except ValueError:
            print("Tipo de dato incorrecto. El ID debe ser un número.")
 

def registrar_evaluacion_modular(datos, trainer):
    campers_asignados_ids = trainer.get("campers_asignados", [])
    
    print("\n--- Registrar Evaluación Modular (Teo, Prac, Quiz) ---")
    print("\nLista de Campers Asignados:")
    for c_id in campers_asignados_ids:
        for camper in datos["campers"]:
            if camper["id"] == c_id:
                print(f"ID: {camper['id']} | Nombre: {camper['nombres']} {camper['apellidos']} | Ruta: {camper.get('ruta', 'N/A')}")
                break
    
    if not campers_asignados_ids:
        print(f"El trainer {trainer['nombre']} no tiene campers asignados.")
        input("Presione Enter para continuar...")
        return
        
    try:
        id_camper = int(input("ID del camper a evaluar: "))
        if id_camper not in campers_asignados_ids:
            print("Error de Permiso: Solo puede evaluar a campers asignados.")
            input("Presione Enter para continuar...")
            return

        id_ruta_input = input("ID de la ruta que cursa el camper: ") 
        id_modulo = input("Nombre del módulo que evalúa (ej: Python): ")        
        nota_teo = float(input("Nota teórica (0-100): "))
        nota_prac = float(input("Nota práctica (0-100): "))
        nota_quiz = float(input("Nota quizzes/trabajos (0-100): "))
        
        if not all(0 <= n <= 100 for n in [nota_teo, nota_prac, nota_quiz]):
            print("Error: Todas las notas deben ser valores entre 0 y 100. Operación cancelada.") 
        else: 
            try:
                id_ruta = int(id_ruta_input)
            except ValueError:
                id_ruta = id_ruta_input 
                
            if registrar_evaluacion(datos, id_camper, id_ruta, id_modulo, nota_teo, nota_prac, nota_quiz):
                print("Evaluación modular registrada con éxito.")
            else:
                print("Error: No se pudo registrar la evaluación. Verifique ID/Ruta/Módulo.")
    except ValueError:
        print("Entrada inválida. Asegúrese de que IDs y notas sean números.") 
        
    input("Presione Enter para continuar...")

def colocar_reporte(datos, trainer): 
    campers_asignados_ids = trainer.get("campers_asignados", [])
    try:
        id_camper = int(input("Ingrese el id del camper: "))
        if id_camper not in campers_asignados_ids:
            print("Error de Permiso: Solo puede generar reportes a campers asignados.")
            input("Presione Enter para continuar...")
            return            
        for camper in datos["campers"]:
            if camper["id"] == id_camper:
                reporte = input(f"Ingrese el reporte al estudiante {camper['nombres']} {camper['apellidos']}: ")
                if "reportes" not in camper:
                    camper["reportes"] = []
                camper["reportes"].append(reporte)
                print(f"Reporte agregado para {camper['nombres']} {camper['apellidos']}.")
                guardar_datos(datos)
                input("Presione Enter para continuar...") 
                return
        print("Camper no encontrado")
        input("Presione Enter para continuar...") 
    except ValueError:
        print("Dato ingresado inválido.")
        input("Presione Enter para continuar...")
    
def ver_info_trainer(trainer):
    if not trainer:
        print("Error: trainer no encontrado.")
        return
    
    print("\n--- Información del Trainer ---")
    print(f"ID: {trainer['id']}")
    print(f"Nombre: {trainer['nombre']}")
    print(f"Especialidad: {trainer['especialidad']}")
    print(f"Teléfono: {trainer['telefono']}")
    print(f"Estado: {trainer['estado']}")
    
    campers_asignados = trainer.get("campers_asignados", [])
    print(f"Campers asignados: {len(campers_asignados)}")
    
def ver_campers_asignados(trainer, datos):
    trainer_id = trainer["id"]
    trainers_data = datos.get("trainers", [])
    current_trainer = next((t for t in trainers_data if t.get('id') == trainer_id), None)
    
    if not current_trainer:
        print("\nError: El perfil del trainer no se encontró en la base de datos.")
        return
    campers_asignados = current_trainer.get("campers_asignados", [])   
    if not campers_asignados:
        print(f"\nEl trainer {current_trainer['nombre']} no tiene campers asignados.")
        return   
    print(f"\n--- Campers asignados a {current_trainer['nombre']} ---")
    campers_data = datos.get("campers", [])
    for camper_id in campers_asignados:
        for camper in campers_data:
            if camper.get('id') == camper_id:
                ruta = camper.get('ruta', 'N/A')                
                print(f"ID: {camper['id']} | Nombre: {camper['nombres']} {camper['apellidos']} | Estado: {camper['estado']} | Ruta: {ruta}")
                break
    input("Presione Enter para continuar...")