import datos

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

def update_city(datos_1):
    datos_1 = dict(datos_1)
    city={}
    
    for i in (datos_1["cities"]):
        city.append(i["codigo_postal"])
        
    print(city)
    
    contador_cities = 0
    city_id = int(input("Ingrese el código postal de la ciudad que desea modificar = "))
    
    for i in (datos_1["cities"]):
            if city_id in city and city_id == i["codigo_postal"]:
                contador_cities += 1
                new_name =str(input("Actualizar el nombre. De lo contrario escriba -0- :"))
                if new_name == "0":
                         print(" ")
                else: i["nombre"]=new_name
                new_population =str(input("Actualizar la poblacion. De lo contrario escriba -0- :"))
                if new_population == "0":
                         print(" ")
                else: i["poblacion"]=new_population
                new_country =str(input("Actualizar el pais. De lo contrario escriba -0- :"))
                if new_country == "0":
                         print(" ")
                else: i["pais"]=new_country
    datos_1["cities"].append(city)
    print("-------------------------------------")
    print("La actualizacion de datos se ha completado con éxito")
    print("-------------------------------------")
    if contador_cities == 0:
        print("Usuario no encontrado")         
    update_city(datos_1)

# Mostrar Ciudades
def mostrar_ciudades(archivo):
    data = datos.cargar_datos(archivo)
    # Comenzar a iterar
    for clave, valor in data.items():
        print("----------------------------------------------------")
        print(f"{clave}:")
        print("----------------------------------------------------")
        for i in valor:
            for k in i.keys():
                print(f"{k}: {i[k]}")
            print("----------------------------------------------------")

