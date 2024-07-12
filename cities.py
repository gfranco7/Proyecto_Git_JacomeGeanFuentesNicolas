def create_city(datos_1):
    datos_1 = dict(datos_1)
    city={}
    try:
        city["codigo_postal"]=input("Ingrese el código postal de la ciudad: ")
    except Exception:
        city["codigo_postal"] = 0
        print("Codigo inválido. Para modificarlo ingrese en la opción -actualizar perfil de usuarios- ")

    city["nombre"]=input("Ingrese el nombre de la ciudad: ")
    city["poblacion"]=input("Ingrese la poblacion de la ciudad: ")
    city["pais"]=input("Ingrese el pais : ")
    
    datos_1["cities"].append(city)
    print("-------------------------------------")
    print("El registro se ha completado con éxito")
    print("-------------------------------------")

