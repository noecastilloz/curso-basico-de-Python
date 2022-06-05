# Declaramos una variable

from errno import EADDRNOTAVAIL

calificacion = input("Introduce tu calificacion de la AZ-900: ")
calificacion = int(calificacion)
if calificacion < 700 : # aqui pregunta si la calificaion es menor a 700 en python indentacion que es un espacio antes que empiese la linea de codigo normalmente se usa el TAB
    print("vesssss, por no estudias") # si e smenor a 700 muestra esto
elif calificacion > 1000 :
    print("MIENTES😠😠😠😠 no puedes sacar mas de mil")
else : # Si no secumple el if anterior, pasa a esta linea
    print("Felicidades, pasas por tu certificado") # se ejecuta si ninguno de los if se cumple

# otro ejemplo verificador de edad

edad = input("Introduce tu edad: ")
edad = int(edad) # casteo
if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 : 
    print("Ni que fueras viajero del tiempo")
else :
    print("No pudes llevarte esos cigarros")
