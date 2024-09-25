def main():
    n = int(input('Digite um número: '))
    if find_in_fibonacci(n):
        print(f'O número {n} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {n} não pertence à sequência de Fibonacci.')

def find_in_fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return True
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    return False

if __name__ == '__main__':
    main()