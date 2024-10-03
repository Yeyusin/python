operacion = input('dime la operacion entre estas "suma","resta","multiplicacion" y "division": ')
numero1 = int(input("dame el primer numero: "))
numero2 = int(input("dame el segundo numero: "))

def operacionSuma (a, b):
    resultado = a + b
    return resultado

def operacionResta (a,b):
    resultado = a - b
    return resultado

def operacionMultiplicacion(a,b):
    resultado = a * b 
    return resultado 

def operacionDivision(a,b):
    resultado = a/b
    return resultado

def calculadora(a,b,operacion):
    if operacion == "suma":
        resultado= operacionSuma(a,b)
        print(resultado)
    
    elif operacion == "resta":
        resultado = operacionResta(a,b)
        print(resultado)

    elif operacion == "multiplicacion":
        resultado = operacionMultiplicacion(a,b)
        print(resultado)
    
    elif operacion == "division":
        resultado = operacionResta(a,b)
        print(resultado)
    
    else:
        print("Por favor, mete una operacion valida de las anteriores descritas")

calculadora (numero1, numero2 , operacion)