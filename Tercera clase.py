import random
#Necesitamos crear con Python un juego clasico de piedra, papel, o tijeras que cumpla con:

# la condicion 1 es que se pueda jugar contra la maquina
#la condicion 2 es que pueda mostrar quien gana
# la condicion 3 es que se pueda repetir el juego
# la condicion 4 es que se usen funciones en su desarrollo
# la condicion 5 es que se haga uso de vectores (arrary)

print ("Juego piedra, papel o tijeras \n____________________________\n")

#Array
options=["piedra", "papel", "tijeras"]

def user():
    #input user
    option_user = input("Elige y escribe una de estas opciones:  \n Piedra \n Papel \n Tijeras \n ->").lower()
    print("user " , option_user)
    
    #option machine
    option_machine = random.choice(options)
    print("machine ", option_machine)
    
    if option_user not in options:
       print("Opcion no valida")
       user()
    else:
        compare(option_machine, option_user)

#Regla
def compare(pc,player):
    #empate!!
    if pc == player:
        print("Empate!!")
    elif player == "piedra" and pc == "tijeras":
        print("Ganaste Humano!!")
    elif player == "papel" and pc == "piedra":
        print("Ganaste Humano!!")
    elif player == "tijeras" and pc == "papel":
        print("Ganaste Humano!!")
    else:
        print("Maquina Gano, tu humano perdiste!!")
        
#user()

def jugar():
    while True:
        user()    
        res = input("Escribe 'S' para volver a jugar o 'N' para terminar  ").lower()
        if res != "s":
            break
jugar()
    