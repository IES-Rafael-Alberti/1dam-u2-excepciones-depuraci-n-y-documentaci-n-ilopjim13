def ordenarMenorMayor(a, total, rango):
    o = 0
    for j in range(0, total - 1):
            if a[rango] > a[rango +1]:
                o = a[rango]
                a[rango] = a[rango + 1]
                a[rango + 1] = o
            rango += 1
    return a


def ordenarLista(a):
    total = len(a)
    rango = 0
    for i in range(0, len(a)):
        ordenarMenorMayor(a, total, rango)
        total -= 1
    return a


def main():
    a = [8, 3, 1, 19, 14]
    print(ordenarLista(a))

if __name__ == "__main__":
    main()