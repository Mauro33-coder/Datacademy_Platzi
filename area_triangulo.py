def run():    
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    área = (base*altura)/2
    área = round(área, 2)
    print("El área del triángulo es: " + str(área) + " área")
    Lado_a = float(input("Ingresa otro lado del triángulo al que llamaremos a: "))  
    Lado_b = float(input("Ingresa el otro lado al que llamaremos b: "))
    if base == Lado_a and base == Lado_b:
        print("Tu triángulo es Equilatero")
    elif base == Lado_a or base == Lado_b:
        print("Tu triángulo es Isósceles")
    elif Lado_a == Lado_b != base:
        print("Tu triángulo es Isósceles")
    else:
        print("Tu triángulo es Escaleno")


if __name__=="__main__":
    run()


    
# Dejo estas líneas con el propósito de que tu lo continues si tienes alguna idea fantástica que 
# Si es así no dudes en hacerlo por favor. Nuestra comunidad es grande por sus ideas y colaboración 😉
    
    
#     Menu= """ 

# Según los datos que ingresaste averiguemos juntos que tipo de triángulo es
# 1. Triángulo Equilatero
# 2. Triángulo Escaleno
# 3. Triángulo Isosceles

# Elegí una opción: """

# opción: 1= int(input(Menu))


