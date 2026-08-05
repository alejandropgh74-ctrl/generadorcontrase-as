password generator.py


print: ("Generador de contraseñas")
print: (---------------------------)

longitud = int(intput("Ingrese la longitud de la contraseña: "))

if longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
elif longitud <= 12:
    print("La longitud de la contraseña es aceptable.")
else:
    print("La longitud de la contraseña es fuerte.")

numeros = input ("¿Desea incluir números? Escriba si o no:")
if numeros == "si":
    print("La contraseña incluirá números.")
else: 
    print("La contraseña incluria numeros.")

    simbolos = input("¿Desea incluir simbolos? Escriba si o no:")

    if simbolos == "si":
        print("La contraseña incluirá símbolos.")
else:
 