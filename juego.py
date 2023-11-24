import sys

def jugar_piedra_papel_tijera(opcion_usuario):
    opciones_validas = ["piedra", "papel", "tijera"]

    if opcion_usuario not in opciones_validas:
        print("Error: Opción no válida. Debes elegir entre 'piedra', 'papel' o 'tijera'.")
        return 0

    import random
    opcion_maquina = random.choice(opciones_validas)

#    print(f"Tú elegiste: {opcion_usuario}")
#    print(f"La máquina eligió: {opcion_maquina}")

    if opcion_usuario == opcion_maquina:
        print("0")
        return 0
    elif (
        (opcion_usuario == "piedra" and opcion_maquina == "tijera") or
        (opcion_usuario == "papel" and opcion_maquina == "piedra") or
        (opcion_usuario == "tijera" and opcion_maquina == "papel")
    ):
        print("1")
        return 1
    else:
        print("0")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Debes proporcionar exactamente una opción ('piedra', 'papel' o 'tijera') como argumento.")
        sys.exit(1)

    opcion_usuario = sys.argv[1].lower()
    resultado = jugar_piedra_papel_tijera(opcion_usuario)

    sys.exit(resultado)
