def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Создаем массив, помечаем все числа как простые
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False  # Помечаем все кратные p как составные
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]  # Возвращаем список простых чисел


def main():
    num = int(input("Введите число\n"))
    print(sieve_of_eratosthenes(num))

if __name__ == '__main__':
    main()

