def conversor(unidad_milla, unidad_kilometros):
    
    millas = input("Coloca ac谩 el valor en " + str(unidad_milla) + " que queres convertir: ")
    millas = float(millas)
    kilometros = millas * unidad_kilometros
    kilometros = round(kilometros, 2)
    kilometros = str(kilometros)
    print("Tenes " + kilometros or millas)

menu = """
Bienvenido al conversor de medidas...est谩s preparado? 馃摕

1- Millas a kilometros 
2- kilometros a millas


Eleg铆 una opci贸n: """

opci贸n = int(input(menu))

if opci贸n == 1:
    conversor("millas", 1.609344)
elif opci贸n == 2:
    conversor("kilometros", 0.621371) 
else:
    print("Ingresa una opci贸n correcta por favor")

# if __name__=="__main__":
#     conversor()

