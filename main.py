#imports
from datos import *
from menu import *
from cities import*


#Constants
RUTA_BASE_DE_DATOS = "cities.json"


datos_1 = cargar_datos(RUTA_BASE_DE_DATOS)


while True:
    menu_principal(datos_1) 
    guardar_datos(datos_1, RUTA_BASE_DE_DATOS)
    
    break
