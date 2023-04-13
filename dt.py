factorservi = 0
def init():
    factorservi = float(input("Ingresar factor de servico entre 1 y 3: "))
    if(factorservi >= 1 and factorservi <= 3):
      cal(factorservi)        
    else:
        print("El factor de servicio no es correcto")
        init()

def cal(parametro):
    caudal = float(input("Ingresar caudal: "))
    tentrada = float(input("Ingresar Temp entrada: "))
    tsalida = float(input("Ingresar Temp salida: "))
    consta1 = 1000
    consta2 = 0.0003069

    tamanioDT = round(caudal*(tentrada - tsalida)*parametro*consta1*consta2)

    print("\n El distrito mide ", tamanioDT , '\n')
    chillers(tamanioDT)

def chillers(tdt):
    print("\n Tamaños de chillers Centrífuos y de Absorción 500TR, 750TR, 1000TR \n")
    print("Favor indicar cantidad y lea con detenimiento \n")
    print("__________________________________________________________ \n")
   
    c500 = int(input("Ingrese cantidad para 500TR centrífugos: "))
    c750 = int(input("Ingrese cantidad para 750TR centrífugos: "))
    c1000 = int(input("Ingrese cantidad para 1000TR centrífugos: "))
    aa500 = int(input("Ingrese cantidad para 500TR Absorción: "))
    a750 = int(input("Ingrese cantidad para 750TR Absorción: "))
    a1000 = int(input("Ingrese cantidad para 1000TR Absorción: "))

    #Operación centrífugos
    totalc= (500*c500)+(750*c750)+(1000*c1000)
    totala= (500*aa500)+(750*a750)+(1000*a1000)
    totales = totala + totalc

    tmax = tdt + (tdt*0.5) #Se comprueba el tamaño maximo de TR
    if totales<=tdt:
        print("\n Las tecnologías seleccionadas no suministran el tamaño del DT \n")
        print("__________________________________________________________ \n")
        chillers(tdt)
    elif totales >= tmax:
        print("\n Las tecnologías seleccionadas superan el tope del DT")
        print("__________________________________________________________ \n")
        chillers(tdt)
    else:
        centrifugos(totalc)
        absorcion(totala)
        
def centrifugos(parametro1):
    
    rp=parametro1*0.3190995427365	
    g=(parametro1*511.13199046407)/1000	
    c=(parametro1*0.0035174111853)*(1925000/0.88)	
    o=c*0.03	
    	
    capex=parametro1*0.0035174111853	
    ft=capex*1000000	
    e=capex*1700000	
    b=capex*2000000
    crearTablas('centri')

def absorcion(parametro2):

    g=(parametro2*511.13199046407)/1000		
    c=((parametro2 * 0.0035174111853)*(1925000/0.88))		
    o=c*0.03		
  		
    capex=parametro2*0.0035174111853		
    ft=(capex*1000000)*1.015		
    b=capex*2000000 		
    crearTablas('abso')

def crearTablas(resp):
    if resp == 'centri':
        print("\n Tabla Centrífugos\n")
        
        from prettytable import PrettyTable	
        # Crear la tabla y agregar encabezados
        tabla = PrettyTable(["Energia", "Emisiones CO2(Tco2 al Mes)", "Capex(Dolares por Megavatios)", "Opex (Dolares al año)"])
        # Agregar filas de datos
        tabla.add_row(["Red Publica", 319, 0, 616153])
        tabla.add_row(["Microturbina a gas", 511, 7694337, 230830])
        tabla.add_row(["Solar Fotovoltaica", 0, 3517411, 44412])
        tabla.add_row(["Energia Eólica", 0, 5979599, 616670])
        tabla.add_row(["Energia Biomasa", 0, 7034822, 433582])
        tabla.add_row(["Toneladas de Refrigeración de los chillers centrifugos seleccionados son:", 1000, "", ""])
        # Mostrar la tabla en la consola
        print(tabla)
        
    elif resp == 'abso':
        print("\n Tabla Absorción")
        
        from prettytable import PrettyTable	
        # Crear la tabla y agregar encabezados
        tabla = PrettyTable(["Energia", "Emisiones CO2(Tco2 al Mes)", "Capex(Dolares por Megavatios)", "Opex (Dolares al año)"])
        # Agregar filas de datos        
        tabla.add_row(["Microturbina a gas", 511, 7694337, 230830])
        tabla.add_row(["Solar Termica", 0, 3570172, 45078])        
        tabla.add_row(["Energia Biomasa", 0, 7034822, 433582])
        tabla.add_row(["Toneladas de Refrigeración de los chillers de absorción seleccionados son:", 1000, "", ""])
        # Mostrar la tabla en la consola
        print(tabla)
        
init()