import random
import re

print("Bienvenide a Piedra,papel,tijeras,lagarto o Spock")
def playersInput():
    try:
        varInput = input("Selecciona el numero de jugadores: ")
        intInput = int(varInput)

        if intInput == 1 or intInput == 2:
            return intInput
        else:
            raise Exception("") 

    except:
        print("Por favor, selecciona un numero valido de jugadores")
        return playersInput()
    
players=playersInput()

def nameInput():
    patron = r"^[a-zA-Z0-9ñ]+$"
    try:
        varInput = input("Selecciona tu nombre: ")
        verifyInput = re.match(patron,varInput)

        if(verifyInput):
            return varInput
        
        else:
            raise Exception("")

    except:
        print("Por favor, no pongas espacios,ni caracteres especiales")
        return nameInput()
    
if players==1:
    name1= nameInput()
    name2= "Maquina"
else:
    name1 = "Jugador 1"
    name2 = "Jugador 2"

opciones = ("piedra","papel","tijera","lagarto","spock")
opcionesStr = ", ".join(opciones)

dicOpciones={
    "piedra":{
        "papel":"Papel envuelve piedra, has perdido",
        "tijera":"Piedra aplasta a tijera, has ganado",
        "lagarto":"Piedra aplasta a lagarto, has ganado",
        "spock": "Spock pulveriza la piedra, has perdido",
    },
    "papel":{
        "piedra":"Papel envuelve piedra, has ganado",
        "tijera":"Tijera corta papel, has perdido",
        "lagarto":"Papel desautoriza Spock, has ganado",
        "spock":"Lagarto devora papel, has perdido"
    },
    "tijera":{
        "piedra":"Piedra aplasta a tijera, has perdido",
        "papel":"Tijera corta papel, has ganado",
        "lagarto":"Tijera decapita lagarto, has ganado",
        "spock": "Spock rompe tijera, has perdido"
    },
    "lagarto":{
        "piedra":"Piedra aplasta lagarto, has perdido",
        "papel":"Lagarto devora papel, has perdido",
        "tijera":"Tijera decapita lagarto, has perdido",
        "spock":"Lagarto envenena Spock, has ganado"
    },
    "spock":{
        "piedra":"Spock vaporiza piedra, has ganado",
        "papel":"Papel desautoriza Spock, has perdido",
        "tijera":"Spock rompe tijera, has ganado",
        "lagarto":"Lagarto envenena Spock, has perdido"
    }
}

def opcionesInput(name):
    #Hardcoded but you could use for pattern patron=r"^"+ "|".join(opciones) + "$"
    patron=r"^(piedra|papel|tijera|lagarto|spock)$"

    try:
        varInput = input(f"{name} selecciona una de las siguientes opciones:{opcionesStr}\n= ")
        verifyInput = re.match(patron,varInput)

        if(verifyInput):
            return varInput
        
        else:
            raise Exception("")

    except:
        print("Por favor, solo pon exactamente una de las opciones descritas")
        
        return opcionesInput(name)

def yesNoInput(text):
    patron= r"^(yes|no)$"
    try:
        varInput=(f"Deseas {text}? \n yes   no \n = ")
        checkInput=re.match(patron,varInput)

        if checkInput:
            return varInput
        else:
            raise Exception("")
    except:
        print("Solo 'yes' or 'no' es aceptado")
        return yesNoInput(text)

def rondas(numero):
    winCondition= (numero/2) + 0.5
    contadorJugador1=0
    contadorJugador2=0

    for i in range(numero):
        print(f"Ronda {i+1} de {numero}")
        seleccionJugador1 = opcionesInput(name1)
        seleccionJugador2=""

        if players == 2:
            print("\n \n \n \n \n \n \n \n")
            seleccionJugador2 = opcionesInput(name2)
        else:
            seleccionJugador2= random.choice(opciones)

            print("la maquina selecciono ",seleccionJugador2)
        
        if(seleccionJugador1==seleccionJugador2):
            print("Empate, se repite la ronda")
            print(f"{name1} V:{contadorJugador1}    {name2} V:{contadorJugador2}")
            i=i-1

        else:
            resultado = dicOpciones[seleccionJugador1][seleccionJugador2]
            patronWin=r"has ganado"

            if re.match(patronWin, resultado):
                if players==2:
                    print(f"{name1} gana")
                else:
                    print(resultado)

                contadorJugador1 +=1
        
                print(f"{name1} V:{contadorJugador1}    {name2} V:{contadorJugador2}")
                
            else:
                if players==2:
                    print(f"{name2} gana")
                else:
                    print(resultado)

                contadorJugador2 +=1

                print(f"{name1} V:{contadorJugador1}    {name2} V:{contadorJugador2}")
                
            if winCondition==contadorJugador1:
                return "jugador1"
            if winCondition==contadorJugador2:
                return "jugador2"
            
def rondasInput():
    patron=r"^[135]$"
    try:
        varInput= input("Seleccione el numero de rondas entre los siguientes modos:\n 1 Ronda 3 Rondas 5 Rondas \n = ")
        checkInput= re.match(patron,varInput)
        varInput = int(varInput)

        if checkInput:
            return varInput
        else:
            raise Exception("")
    
    except:
        print("Por favor, pon el numero solo de las rondas")
        return rondasInput()
            
def play():
    status=1

    numeroRondas = rondasInput()

    while status:
        wStreak=0
        resultado=rondas(numeroRondas)

        if "jugador1" in resultado:
            print("Has ganado la partida")
            
            wStreak+=1
        
            print("Llevas esta racha de Victorias ",wStreak)
        else:
            print("Has perdido la partida")

            wStreak=0
        
        continuar= yesNoInput("continuar")

        if continuar=="no":
            status=0

        if(continuar=="yes"):
            modo= yesNoInput("cambiar de modo")
        
            if modo=="yes":
                numeroRondas=rondasInput()
play()

print("Juego finalizado, gracias por jugar")
