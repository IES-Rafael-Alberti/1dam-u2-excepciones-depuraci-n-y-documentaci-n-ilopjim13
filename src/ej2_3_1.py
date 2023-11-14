#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def  edades(edad):
    """Imprime 1 a 1 todos los años que ha cumplido hasta la edad indicada"""
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
        edades(edad)
    except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()


