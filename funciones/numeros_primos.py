def is_prime(num):
    if num <= 1:
        return False

    n = 2
    while n <= num ** .5:
        if num % n == 0:
            return False
        n += 1

    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
