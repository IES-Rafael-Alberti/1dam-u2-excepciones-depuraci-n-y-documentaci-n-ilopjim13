# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def cuentaAtras(num):
    """Imprime 1 a 1 desde el número introducido hasta 0 separado por coma"""
    if num <= 0:
        raise ValueError('El número no puede ser negativa: ' + str(num))
    for i in range(num, -1, -1):
        if i > 0:
            print(i,end=", ")
        if i == 0:
            print(i)
    return i

def main():
    while True:
        try:
            num = int(input("Introduce un número: "))
            cuentaAtras(num)
        except ValueError as e:
            print(e)
        else:
            if num > 0:
                break

if __name__ == "__main__":
    main()