print("Generador de contraseñas")
print("---------------------------")

longitud = int(input("Ingrese la longitud de la contraseña: "))

# Valida que la longitud mínima de la contraseña sea de 8 caracteres
while longitud < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    longitud = int(input("Ingrese nuevamente la longitud: "))

print("Longitud valida.")

# Clasifica la longitud ingresada como aceptable o fuerte
if longitud <= 12:
    print("La longitud de la contraseña es aceptable.")
else:
    print("La longitud de la contraseña es fuerte.")

numeros = input("¿Desea incluir números? Escriba si o no: ").strip().lower()

# Evalúa si el usuario desea incluir números
if numeros == "si":
    print("La contraseña incluirá números.")
else:
    print("La contraseña no incluirá números.")

simbolos = input("¿Desea incluir símbolos? Escriba si o no: ").strip().lower()

# Evalúa si el usuario desea incluir símbolos
if simbolos == "si":
    print("La contraseña incluirá símbolos.")
else:
    print("La contraseña no incluirá símbolos.")

print("Configuración terminada.")
print("La generación de la contraseña se implementará en la siguiente etapa.")
