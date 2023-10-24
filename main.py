#1.

#a)
def S(n):
    if n == 1:
        return 10
    else:
        return S(n - 1) + 10

user = int(input())
print(S(user))

#b)
def A(n):
    if n == 1:
        return 2
    else:
        return A(n - 1)**(-1)

#c)
def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) + n**2

#d)
def P(n):
     if n == 1:
        return 1
     else:
         return n**2 * P(n-1) + (n-1)

#e)
def D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

#f)
def W(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return W(n - 1) * W(n - 2)

#g)
def T(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)

#2.
def PG(a, r, n):
    if n == 1:
        return a
    else:
        return PG(a, r, n - 1) * r

#3.
def PertAT(n):
    if n == 2:
        return True
    if n < 2:
        return False
    return (PertAT(n - 3)
or PertAT(n / 2))

numeros = [6, 7, 19, 12]

for n in numeros:
    if PertAT(n):
        print(f'{n} pertence a T')
    else:
        print(f'{n} não pertence a T')

#4.
def PertAM(n):
    if n == 2 or n == 3:
        return True
    elif n <= 0:
        return False
    elif n % 2 == 0:
        return PertAM(n // 2)
    elif n % 3 == 0:
        return PertAM(n // 3)
    else:
        return False

numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for numero in numeros:
    if PertAM(numero):
        print(f'{numero} pertence a M.')
    else:
        print(f'{numero} NÃO pertence a M.')

#5.
def PertAS(s):
    if s == "a" or s == "b":
        return True
    if s.endswith("b"):
        prefix = s[:-1]
        return PertAS(prefix)
    return False

cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]

for cadeia in cadeias:
    if PertAS(cadeia):
        print(f'"{cadeia}" pertence a S.')
    else:
        print(f'"{cadeia}" NÃO pertence a S.')

#6.
def PertAW(s):
    if s == "a" or s == "b" or s == "c":
        return True
    if s.startswith("a") and s.endswith("c"):
        inner_part = s[1:-1]
        return PertAW(inner_part)
    return False

cadeias = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]

for cadeia in cadeias:
    if PertAW(cadeia):
        print(f'"{cadeia}" pertence a W.')
    else:
        print(f'"{cadeia}" NÃO pertence a W.')

#7.
def binarias_impares_zeros(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]

    with_zero = ["0" + s for s in binarias_impares_zeros(n - 1)]
    without_zero = ["1" + s for s in binarias_impares_zeros(n - 1)]

    return with_zero + without_zero


n = 3
resultado = binarias_impares_zeros(n)

for cadeia in resultado:
    print(cadeia)

#8.

#a) Sequência: 1, 3, 9, 27,...

def sequencia_a(n):
    if n == 1:
        return 1
    else:
        return 3 ** (n - 1)


#b) Sequência: 2, 1, 1/2, 1/4,...

def sequencia_b(n):
    if n == 1:
        return 2
    else:
        return 1 / sequencia_b(n - 1)


#c) Sequência: a, b, a + b, a + 2b, 2a + 3b,...

def sequencia_c(n, a, b):
    if n == 1:
        return a
    if n == 2:
        return b
    return sequencia_c(n - 1, a, b) + sequencia_c(n - 2, a, b)


#d) Sequência: p, p-q, p+q, p-2q, p+2q, p-3q,...

def sequencia_d(n, p, q):
    if n == 1:
        return p
    if n % 2 == 0:
        return sequencia_d(n - 1, p, q) + 2 * q
    else:
        return sequencia_d(n - 1, p, q) - 2 * q

#9.
def numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n - 1)

n = 5
resultado = numero_triangular(n)
print(f"O {n}-ésimo número triangular é {resultado}")

#10.

#a)
def populacao_bacterias(n):
    if n == 0:
        return 50000
    else:
        return 3 * populacao_bacterias(n - 1)

#b)
populacao_desejada = 200000
n = 0
populacao_atual = 50000

while populacao_atual <= populacao_desejada:
    n += 1
    populacao_atual = 3 * populacao_atual

print(f"A população excederá {populacao_desejada} bactérias após {n} leituras.")

#11
def Rotina(L, j):
    if j == 1:
        return L
    else:
        i = L.index(max(L[:j]))
        L[i], L[j - 1] = L[j - 1], L[i]
        return Rotina(L, j - 1)

L = [3, 7, 4, 2, 6]
resultado = Rotina(L, 5)

print("Lista L após a chamada Rotina:", resultado)
print("Total de chamadas realizadas à Rotina:", len(resultado))






