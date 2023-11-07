# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.

def cuentaAtras(num, xd):
    if num <= 0:
        raise ValueError('El número no puede ser negativa: ' + str(num))
    for i in range(num, -1, -1):
        if i > 0:
            print(i,end=", ")
        if i == 0:
            print(i)

def main():
    xd = 0
    while xd == 0:
        try:
            num = int(input("Introduce un número: "))
            cuentaAtras(num, xd)
        except ValueError as e:
            print(e)




if __name__ == "__main__":
    main()