operacion = input('dime la operacion entre estas "suma","resta","multiplicacion"y "division": ')
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

operaciones = {
    "suma":operacionSuma,
    "resta":operacionResta,
    "multiplicacion":operacionMultiplicacion,
    "division":operacionDivision
}

def calculadora(a,b,operacion):
    calculador = operaciones[operacion]

    resultado = calculador(a,b)

    print(resultado)

calculadora (numero1, numero2 , operacion)