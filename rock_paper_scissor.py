import random

# Variables globales
nombre = ""
userScore = 0
cpuScore = 0
tie = 0

def comparison(myChoice, cpuChoice):
    global userScore
    global cpuScore
    global tie
    # Comparison
    if myChoice == "piedra" and cpuChoice == "papel":
        cpuScore = cpuScore + 1
    elif  myChoice == "piedra" and cpuChoice == "tijeras":
        userScore = userScore + 1
    elif myChoice == "papel" and cpuChoice == "tijeras":
        cpuScore = cpuScore + 1
    elif myChoice == "papel" and cpuChoice == "piedra":
        userScore = userScore + 1 
    elif  myChoice == "tijeras" and cpuChoice == "piedra":
        cpuScore = cpuScore + 1  
    elif  myChoice == "tijeras" and cpuChoice == "papel":
        userScore = userScore + 1
    else:
        tie = tie + 1

    # Scores
    if userScore > cpuScore and tie < userScore:
        print("Ganaste " + nombre + " !")
    elif cpuScore > userScore and tie < cpuScore:
        print("Has sido derrotad@!")
    elif cpuScore == userScore and tie < cpuScore:
        print("Hubo empate")
    elif tie >= userScore and tie >= cpuScore:
        print("Hubo empate")


def game():
    # Definición de variable
    global nombre
    cpuOptions = ["piedra", "papel", "tijeras"]
    jugar = True
    myChoice = ""
    found = False
    cpuChoice = ""
    continuar = ""

    nombre = input("Ingrese su nombre: ")
    while jugar == True:
        myChoice = ""
        cpuChoice = ""
        while found == False:
            myChoice = input("Ingrese piedra, papel o tijeras:\n")
            for i in cpuOptions:
                if myChoice == i:
                    found = True
            
            if found == False:
                print("Oh no! La opcion seleccionada no es valida.")
        
        print("--------Match--------")
        cpuChoice = random.choice(cpuOptions)
        print(myChoice +  "vs" + cpuChoice)
        comparison(myChoice, cpuChoice)
        print("---------------------")
        continuar = input("Deseas continuar jugando? s/n \n")
        if continuar == "n":
            jugar = False
            print("Gracias por jugar!")
        else:
            found =  False
        
            

if __name__ == '__main__':
    game()