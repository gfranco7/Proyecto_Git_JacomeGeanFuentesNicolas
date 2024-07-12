import json, os , time, traceback, datetime

def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()

# Capturar excepciones
def capturarException(exception):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear el mensaje de error con la fecha y hora
    mensaje_error = (f"Fecha y hora: {fecha_actual}\n")
    mensaje_error += traceback.format_exc()  # Agregar el traceback de la excepción
    
    # Guardar el mensaje de error en un archivo de texto
    with open("exceptions.txt", "a") as file:
        file.write(mensaje_error + "\n")


    os.system("cls")
    print("----------------")        
    print("VALOR INCORRECTO")
    print("----------------")
    os.system("cls")
    time.sleep(2)   
