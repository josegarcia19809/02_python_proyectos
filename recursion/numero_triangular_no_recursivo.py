def suma_triangular(n: int) -> int:
    total: int = 0
    for i in range(n, 0, -1):
        print(i, end=" ")
        total += i
    print()
    return total


print(suma_triangular(6))



