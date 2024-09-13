print (" sistema para calcular promedio de un alumno ")

nombre = input("cual es tu nombre? : ")

print (nombre + (" inserta tus calificaciones de las siguientes materias") )

matematicas = bool(input("matematicas: ") )
ingles = bool(input("ingles: ") )
naturales = bool(input("naturales: ") )

promedio = (matematicas + ingles + naturales) / 3


if promedio >= 3:
    print (nombre + ", pasaste el año con un promedio de: ",  promedio )

print ("fin.")

if promedio <= 2:
    print (nombre + ", perdiste el año con un promedio de: ",  promedio )
    print ("fin")
    
   
