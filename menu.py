from cities import *
def menu_principal(datos_1):
    while True: 
        print("- -  Bienvenido al sistema  - -")
        print("- -  [1] Para agregar una ciudad - -")
        print("- -  [2] Para modificar información de una ciudad - -")
        print("- -  [3] Para ver informe de ciudades - -")
        print("- -  [4] Para salir del sistema - -")
        opcion = int(input("- -  Ingrese la opcion deseada - : "))
        if opcion == 1:
            create_city(datos_1)
        elif opcion == 2:
            update_city(datos_1)
        elif opcion == 3:
            reporte_ciudades(datos_1)
        elif opcion == 4:
            print(" -- Saliendo del sistema... --")
            break

    