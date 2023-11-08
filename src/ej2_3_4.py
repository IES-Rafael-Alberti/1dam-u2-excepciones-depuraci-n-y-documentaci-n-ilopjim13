# Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def esEntero(num):
    """Imprime 'Bieen' si el número entero y si no lo es dará una excepción"""
    num = int(num)
    menor = num <= 0
    mayor = num > 0
    if menor == True or mayor == True:
        print("Bieen")
        return "Bieen"

def main():
    num = input("Introduce un número entero: ")
    try:
        esEntero(num)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print("La entrada no es correcta")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()