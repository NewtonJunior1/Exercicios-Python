'''1)	Faça um programa que carregue uma matriz 3x5
com números inteiros, calcule e mostre a quantidade de
elementos entre 15 e 20.'''

valor = 0
conta = 0
matriz = [[0] * 5 for i in range(3)]
for l in range(3):
    for c in range(5):
        print("Digite um numero")
        matriz[l][c] = int(input())
        if matriz[l][c] >= 15 and matriz[l][c] <= 20:
            conta = conta + 1
for l in range(3):
    for c in range(5):
        print(matriz[l][c], end=" ")
    print()
print("A quantidade de elementos maior que 15 e menor que 20 é:",conta)

