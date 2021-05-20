def menu():
        resp="s"
        num=0
        cal=[]

        while resp=="s" or resp=="S":

                opcion=0
        print("(1) Calcular volumen de un cilíndro: ")
        print("(2) Calcular volumen de un esfera: ")
        print("(3) Calcular volumen de un cono: ")
        print("(4) Calcular volumen de un pirámide: ")
        print("(5) Calcular volumen de un rectángulo: ")
        print("(6) Calcular volumen de un cubo: ")

        opcion = input("Ingrese la opción que deseas calcular: ")

        if opcion=="1":
                cilindro(cal)
        elif opcion=="2":
                esfera(cal)
        elif opcion=="3":
                cono(cal)
        elif opcion=="4":
                piramide(cal)
        elif opcion=="5":
                cubo(cal)

        resp = input("Desea realizar otro cálculo? s/n: ")

def cilindro(cal):

        radio = float(input("Ingresa el rádio de si cilíndro: "))
        altura = float(input("Ingresa la altura de tu cilíndro: "))
        pi=3.1415926536

        volumen=pi*(radio**2)*altura
        volumen=round(volumen, 2)

        print("El volúmen del cilíndro es: ", str(volumen))

def esfera(cal):

        radio = float(input("Ingresa el rádio de tu esfera: "))
        pi=3.1415926536
        
        volumen=4/3*pi*radio**3
        volumen=round(volumen, 2)
        
        print("El volúmen de tu esfera es: ", str(volumen))

def cono(cal):

        radio = float(input("Ingresa el rádio de tu cono: "))
        altura = float(input("Ingresa la altura de tu cono: "))
        pi=3.1415926536

        volumen=1/3*pi*radio**2*altura
        volumen=round(volumen, 2)

        print("El volúmen de un cono es: ", str(volumen))

def piramide(cal):

        lado = float(input("Ingresa uno de los lados de la pirámide: "))
        altura = float(input("Ingresa la altura de la piramide: "))
        areabase = lado*lado
        
        volumen = ((areabase * altura)) / 3
        volumen=round(volumen, 2)
        
        print("El volúmen de la piramide es: ", str(volumen))

def cubo(cal):

        lado = float(input("Ingresa uno de los lados del cubo: "))
                
        volumen = lado**3
        volumen=round(volumen, 2)
        
        print("El volúmen de la piramide es: ", str(volumen))

menu ()