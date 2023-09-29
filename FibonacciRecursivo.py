def lin(texto):
    print('~'*20)
    print(texto)
    print('~'*20)

lin("Fibonacci Recursivo")

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(int(input('Digite um numero: ')))
print(result)
