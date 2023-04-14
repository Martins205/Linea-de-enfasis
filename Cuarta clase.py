import random


class JuegoPPT:
    
    def __init__(self):
       self.options=["piedra", "papel", "tijeras"]
       self.res =["s", "n"]
       
    def jugar(self):
     while True:
        self.user()
        res = input("Escribe 'S' para volver a jugar o 'N' para terminar  ").lower()
        if res not in self.res:          
           print("Opcion no valida ")            
        elif res != "s":
         break
      
       
    def user(self):
    #input user
     option_user = input("Elige y escribe una de estas opciones:  \n Piedra \n Papel \n Tijeras \n ->").lower()
     print("user " , option_user)
    
    #option machine
     option_machine = random.choice(self.options)
     print("machine ", option_machine)
    
     if option_user not in self.options:
       print("Opcion no valida")
       self.user()
     else:
       self.compare(option_machine, option_user)
       
       
    def compare(self, pc, player):    
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
        
juego = JuegoPPT()
juego.jugar()
