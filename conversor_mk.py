def conversor(unidad_milla, unidad_kilometros):
    
    millas = input("Coloca acá el valor en " + str(unidad_milla) + " que queres convertir: ")
    millas = float(millas)
    kilometros = millas * unidad_kilometros
    kilometros = round(kilometros, 2)
    kilometros = str(kilometros)
    print("Tenes " + kilometros or millas)

menu = """
Bienvenido al conversor de medidas...estás preparado? 📟

1- Millas a kilometros 
2- kilometros a millas


Elegí una opción: """

opción = int(input(menu))

if opción == 1:
    conversor("millas", 1.609344)
elif opción == 2:
    conversor("kilometros", 0.621371) 
else:
    print("Ingresa una opción correcta por favor")

# if __name__=="__main__":
#     conversor()

