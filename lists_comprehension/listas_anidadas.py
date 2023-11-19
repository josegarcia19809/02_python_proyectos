matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])  # 2
print(matriz[1][-1])  # 6
print(matriz[-1])  # [7, 8, 9]
print(matriz[-1][1])  # 8
print(matriz[-1][-2])  # 8
print(matriz[2][-2])  # 8
print(matriz[2][1])  # 8

# Imprimir los valores
for i in matriz:
    for valor in i:
        print(valor, end=" ")  # 1 2 3 4 5 6 7 8 9

print()
[[print(valor) for valor in i] for i in matriz]

tablero = [[num for num in range(1, 4)] for i in range(1, 4)]
print(tablero)

otro_tablero = [["x" if num % 2 == 0 else "o" for num in range(1, 4)] for i in
                range(1, 4)]
print(otro_tablero)
