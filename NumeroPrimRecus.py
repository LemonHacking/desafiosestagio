# Desafio 2

def teste_divisibilidade(A,B):
    if B==1: return 0
    elif A%B==0: return 1
    else: return teste_divisibilidade(A, B-1)


def teste_primalidade(N):
    if teste_divisibilidade(N, N-1)==0: return 1
    else: return 0

def gerar_primos(N,K,M,vetor):
    if teste_primalidade(M)==1:
        vetor.append(M)
        K+=1
    if N==K: return
    else: return gerar_primos(N,K,M+1,vetor)
v = []
result = gerar_primos(int(input("Digite um numero: ")),0,2,v)
print("Números primos em ordem crescente: {}".format(v))