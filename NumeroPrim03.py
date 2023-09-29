#Desafio 1
def testPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    for c in range (2, int(num**0.5) +1 ):
        if num % c == 0:
            return False
    return True

try:
    limit_max = int(input("Digite um número: "))

    prime_numbers = []
    n_prime_numbers = []

    for number in range(2, limit_max + 1):
        if (testPrime(number)):
            prime_numbers.append(number)
        else:
            n_prime_numbers.append(number)
    print("Até o número {}, temos os seguintes números primos: {}".format(limit_max, prime_numbers))
    print("Logo, os números {} NÃO são primos.".format(n_prime_numbers))

except ValueError:
    print("Por favor, insira um número válido.")