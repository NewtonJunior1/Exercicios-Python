'''1)	Faça um programa que receba a quantidade de peças vendidas por vendedor
e armazene essas quantidades em um vetor. Receba também o preço da peça vendida
de cada vendedor e armazene esses preços em outro vetor.
Existem apenas dez vendedores e cada vendedor pode vender apenas um tipo de peça,
isto é, para cada vendedor existe apenas um preço.
Calcule e mostre a quantidade total de peças vendidas por todos os vendedores
e para cada vendedor calcule e mostre o valor total da venda,
isto é, a quantidade de peças * o preço da peça.'''

vende = [0] * 10
preco = [0] * 10
v = 0
valvenda = 0
numvendedor = 0
soma = 0
for i in range(10):
    v = v + 1
    print("Quantas peças foram vendidas pelo vendedor",v, "?")
    vende[i] = int(input())
    soma = vende[i] + soma
    print("qual o valor da peça vendida?")
    preco[i] = int(input())
    for j in range(1):
        numvendedor = numvendedor + 1
        valvenda = vende[i] * preco[i]
        print("o valor da venda do vendedor",numvendedor,"foi",valvenda)
print("A quantidade de peças vendidas foram",soma)
    

