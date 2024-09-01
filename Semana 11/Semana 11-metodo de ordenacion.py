# ordenacion_matriz.py

def bubble_sort(fila_actual):
    n = len(fila_actual)
    for i in range(n):
        for j in range(n - i - 1):
            if fila_actual[j] > fila_actual[j + 1]:
                fila_actual[j], fila_actual[j + 1] = fila_actual[j + 1], fila_actual[j]


if __name__ == "__main__":
    matriz = [
        [9, 1, 3],
        [4, 7, 2],
        [6, 5, 8]
    ]

    fila_a_ordenar = 0
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    bubble_sort(matriz[fila_a_ordenar])

    print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
    for fila in matriz:
        print(fila)
