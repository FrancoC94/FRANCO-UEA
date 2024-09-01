# busqueda_matriz.py

def buscar_valor(valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    valor_a_buscar = 5
    resultado = buscar_valor(valor_a_buscar)

    if resultado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
