# Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"

def contraseñaCorrecta(contra, psw):
    if contra != psw:
        raise NameError("Incorrect Password!!")
    else:
        print("Correct Password!!")

def main():
    psw = "contra"
    try:
        contra = input("Introduce la contraseña: ")
        contraseñaCorrecta(contra, psw)
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()