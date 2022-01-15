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
  
  win_round = False
  tie_round = False

  
  # Comparisons
  if myChoice == "piedra" and cpuChoice == "papel":
    cpuScore = cpuScore + 1
  elif  myChoice == "piedra" and cpuChoice == "tijeras":
    userScore = userScore + 1
    win_round = True
  elif myChoice == "papel" and cpuChoice == "tijeras":
    cpuScore = cpuScore + 1
  elif myChoice == "papel" and cpuChoice == "piedra":
    userScore = userScore + 1 
    win_round = True
  elif  myChoice == "tijeras" and cpuChoice == "piedra":
    cpuScore = cpuScore + 1  
  elif  myChoice == "tijeras" and cpuChoice == "papel":
    userScore = userScore + 1
    win_round = True
  else:
    tie = tie + 1
    tie_round = True

      
      
  if win_round == True:
    print("Ganaste " + nombre + "!")
  elif tie_round == True:
    print("Hubo empate")
  else:
    print("Has sido derrotad@!") 
      
      
      
def game():
  # Definición de variable
  global nombre
  jugar = True
  
  
  cpuOptions = ["piedra", "papel", "tijeras"]
  nombre = input("Ingrese su nombre: ")
  while jugar == True:
    myChoice = input("Ingrese piedra, papel o tijeras:\n")
    print("--------Match--------")
    cpuChoice = random.choice(cpuOptions)
    print(myChoice +  " vs " + cpuChoice)
    comparison(myChoice, cpuChoice)
    print("---------------------")
    continuar = input("Deseas continuar jugando? s/n \n")
    if continuar == 'n':
      jugar = False
      print("Gracias por jugar!")
  
  
  
game()
  
