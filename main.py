print("Generador de contraseñas")
print("---------------------------")

longitud = int(input("Ingrese la longitud de la contraseña: "))

while longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    longitud = int(input("Ingrese nuevamente la longitud: "))

print("Longitud valida.")

if longitud <= 12:
    print("La longitud de la contraseña es aceptable.")
else:
    print("La longitud de la contraseña es fuerte.")

numeros = input("¿Desea incluir números? Escriba si o no: ").strip().lower()
while numeros != "si" and numeros != "no":
    print("Respuesta no valida")
    numeros = input("Escriba unicamente si o no:").strip().lower()

if numeros == "si":
    print("La contraseña incluirá números.")
else:
    print("La contraseña no incluirá números.")

simbolos = input("¿Desea incluir símbolos? Escriba si o no: ").strip().lower()
while simbolos != "si" and simbolos != "no":
    print ( "Respuesta no validad")
    simbolos = input ("Esrciba unicamente si o no:").strip().lower()
if simbolos == "si":
    print("La contraseña incluirá símbolos.")
else:
    print("La contraseña no incluirá símbolos.")

print("Configuración terminada.")
print("La generación de la contraseña se implementará en la siguiente etapa.")

#caracteres para generar la contraseña
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros_disponibles = "0123456789"
simbolos_disponibles = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

#Las letras se incluyen siempre

caracteres = minusculas + mayusculas

# Se agregan números si el usuario los seleccionó
if numeros == "si":
    caracteres = caracteres + numeros_disponibles

# Se agregan símbolos si el usuario los seleccionó
if simbolos == "si":
    caracteres = caracteres + simbolos_disponibles

#Letras → siempre
#Mayúsculas → siempre
#Números → opcionales
#Símbolos → opcionales

print (caracteres)
caracter_aleatorio = random.choice(caracteres)

print(caracter_aleatorio)
