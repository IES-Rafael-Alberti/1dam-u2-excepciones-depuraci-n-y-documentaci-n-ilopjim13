# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def impares(num):
    """Imprime todos números impares hasta el número indicado separados por coma."""
    if num <= 0:
        raise ValueError('El número no puede ser negativa: ' + str(num))
    for i in range(1, num + 1, 2):
        if i < num - 1:
            print(i, end=", ")
        if i == num or i == num - 1:
            print(i)
    return i

def main():
    try:
        num = int(input("Introduce un número: "))
        impares(num)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
