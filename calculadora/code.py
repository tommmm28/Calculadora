num1 = int(input("Ingresa el primer numero"))
num2 = int(input("Ingresa el primer numero"))

operacion = input("Ingresa la operacion a realizar")

while True:
    if operacion == "suma":
       print("Operacion suma:")
       print(num1 + num2)
    elif operacion == "resta":
        print("Operacion resta:")
        print(num1 - num2)
    elif operacion == "division":
        print("Operacion division:")
        print(num1 / num2)
    elif operacion == "multiplicacion":
        print("Operacion multiplicacion:")
        print(num1 * num2)
    else: 
        print("Signo invalido")
        """continuar = input("Desea continuar? si/no") 
        if continuar == "no":
            break"""