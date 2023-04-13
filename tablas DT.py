from prettytable import PrettyTable	
# Crear la tabla y agregar encabezados
tabla = PrettyTable(["Tabla Centrífugos"])
tabla = PrettyTable(["Energia", "Emisiones CO2(Tco2 al Mes)", "Capex(Dolares por Megavatios)", "Opex (Dolares al año)"])
# Agregar filas de datos
tabla.add_row(["Red Publica", 319, 0, 616153])
tabla.add_row(["Microturbina a gas", 511, 7694337, 230830])
tabla.add_row(["Solar Fotovoltaica", 0, 3517411, 44412])
tabla.add_row(["Energia Eólica", 0, 5979599, 616670])
tabla.add_row(["Energia Biomasa", 0, 7034822, 433582])
tabla.add_row(["Toneladas de Refrigeración de los chillers seleccionados son:", 1000, "", ""])
# Mostrar la tabla en la consola
print(tabla)