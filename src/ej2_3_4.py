# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def entero(num):
    num = int(num)
    menor = num <= 0
    mayor = num > 0
    if menor == True or mayor == True:
        print("Bieen")

def main():
    num = input("Introduce un número entero: ")
    try:
        entero(num)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print("La entrada no es correcta")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()