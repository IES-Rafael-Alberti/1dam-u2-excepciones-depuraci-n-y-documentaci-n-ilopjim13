#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def  edades(edad):
    """hola"""
    if edad <= 0:
        raise ValueError('Edad no puede ser negativa: ' + str(edad))
    for i in range(1,edad + 1):
        if i < edad:
            print(i,end=" ")
        if i == edad:
            print(i)
    return i


def main():
    try:
        edad= int(input("Introduce tu edad: "))
    except ValueError as e:
        if edad == str:
            print("Error, error debe ser un número")
        else:
            print(e)
    edades(edad)

if __name__ == "__main__":
    main()


