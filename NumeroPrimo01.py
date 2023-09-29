#Desafio 3

n = int(input("Digite um número: "))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[32m", end="")
        total += 1
    else:
        print("\033[31m", end="")

    print("{} ".format(c), end="")
print("\n\033[m O número {}, foi dívisivel {} vezes, portanto...".format(n, total))
if total == 2:
    print("\033[32m ELE É UM NÚMERO PRIMO!".format(n))
else:
    print("\033[31m ELE NÃO É UM NÚMERO PRIMO!")
