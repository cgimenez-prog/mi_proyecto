def filtrar_pares(lista):
    # Recibe una lista y devuelve los números pares
    r = []
    for num in lista:
        if num % 2 == 0:
            r.append(num)
    return r
