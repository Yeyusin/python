opciones= ("suma","resta","multiplicacion","division")

opcionesStr=" "    

for i in range(len(opciones)):
    if len(opciones) -1 != i: 
        opcionesStr = opcionesStr + opciones[i] + ", "

    else:
        opcionesStr += opciones[i]     

def recogidaOpcion():
    try:
        opcion= input(f"Selecciona una de las siguientes opciones{opcionesStr}: ")
        if len(opcion)==0:
            raise Exception("Por favor, rellena el input")
        if opcion not in opciones:
            raise Exception("Por favor, solo puedes selecciona una de las siguientes opciones descritas")
        
    except Exception as error:
        print(error.args)
        return recogidaOpcion()
    
    else:
         for i in range(len(opciones)):
            if opciones[i] in opcion:
                return opciones[i]

opcionSelecionada = recogidaOpcion() 

print(opcionSelecionada)
