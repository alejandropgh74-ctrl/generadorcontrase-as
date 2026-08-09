# Muestra el nombre del programa
print("Generador de contraseñas")
print("---------------------------")

# Solicita al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Comprueba que la contraseña tenga mínimo 8 caracteres
while longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    longitud = int(input("Ingrese nuevamente la longitud: "))

print("Longitud valida.")

# Evalúa la longitud ingresada
if longitud <= 12:
    print("La longitud de la contraseña es aceptable.")
else:
    print("La longitud de la contraseña es fuerte.")

# Pregunta si se desean incluir números
numeros = input("¿Desea incluir números? Escriba si o no: ").strip().lower()

if numeros == "si":
    print("La contraseña incluirá números.")
else:
    print("La contraseña no incluirá números.")

# Pregunta si se desean incluir símbolos
simbolos = input("¿Desea incluir símbolos? Escriba si o no: ").strip().lower()

if simbolos == "si":
    print("La contraseña incluirá símbolos.")
else:
    print("La contraseña no incluirá símbolos.")

# Indica que la configuración inicial ha terminado
print("Configuración terminada.")
print("La generación de la contraseña se implementará en la siguiente etapa.")
