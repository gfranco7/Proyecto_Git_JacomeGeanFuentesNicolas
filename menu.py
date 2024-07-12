from cities import *
def menu_principal(datos_1):
    print("- -  Bienvenido al sistema  - -")
    print("- -  [1] Para agregar una ciudad - -")
    print("- -  [2] Para modificar información de una ciudad - -")
    print("- -  [3] Para ver informe de ciudades - -")
    print("- -  [3] Para ver informe de ciudades - -")
    opcion = int(input("- -  Ingrese la opcion deseada - : "))
    if opcion == 1:
        create_city(datos_1)
    else: print("-----------------------------------------------------------------")