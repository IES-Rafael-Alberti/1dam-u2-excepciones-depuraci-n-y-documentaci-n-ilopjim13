# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"

def contraseñaCorrecta(contra):
    """Imprime si la contraseña es correcta y si no lo es dará una excepción"""
    psw = "contra"
    if contra != psw:
        raise NameError("Incorrect Password!!")
    else:
        print("Correct Password!!")
        return "Correct Password!!"

def main():
    try:
        contra = input("Introduce la contraseña: ")
        contraseñaCorrecta(contra)
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()