class persona:
    def __init__(self, nombre, fecha_nac, cedula):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.cedula = cedula
        self.nivel_energia = 80
    #Recuperacion de energia    
    def comerSano(self):
             print(f"{self.nombre} esta comiendo sano")
             self.nivel_energia += 30
             print("Tu nivel de energia subio a: ", self.nivel_energia)
             
    def dormir(self):
             print(f"{self.nombre} esta durmiendo")
             self.nivel_energia += 100
             print("Tu nivel de energia subio a: ", self.nivel_energia)
             
    def comerSinRestri(self):
             print(f"{self.nombre} esta comiendo sin restricciones")
             self.nivel_energia += 75
             print("Tu nivel de energia subio a: ", self.nivel_energia)
             
    #perdida de energia
    
    def correr(self):
             print(f"{self.nombre} esta corriendo")
             self.nivel_energia -= 20
             if self.nivel_energia <= 40:
                #self.nivel_energia = 0
                print(f"Esta por debajo se puede desmallar o podria morir: ", self.nivel_energia)
             else:   
                 print(f"Tu nivel de energioa actual es: ", self.nivel_energia) 
                
Ejecutar = persona("Martin", "12-07-1192", "1115")

Ejecutar.correr()