'''2)	Faça um programa que receba as vendas semanais (de um mês)
de cinco vendedores de uma loja e armazene essas vendas em uma matriz. Calcule e mostre:
a.	O total de vendas do mês de cada vendedor
b.	O total de vendas de cada semana (todos os vendedores juntos)
c.	O total de vendas do mês'''
vendedor = 0
somat = 0
matriz = [[0] * 4 for i in range(5)]
for l in range(5):
    vendedor += 1
    somal = 0
    for c in range(4):
        print("Qual a quantidade de vendas da semana do vendador",vendedor,"?")
        matriz[l][c] = int(input())
        somal = matriz[l][c] + somal
        somat = matriz[l][c] + somat
    print("As vendas mensais do vendedor", vendedor,"é",somal)
for l in range(5):
    for c in range(4):
        print(matriz[l][c], end = " ")
    print()
contador = 1
while contador < 5:
    somac = 0
    for i in range(5):
        x = 0
        somac = somac + matriz[i][x]
    print("O total de vendas da semana",contador,"foi",somac)
    contador += 1
print("As vendas mensais são", somat)
