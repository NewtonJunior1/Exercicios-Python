'''1)	Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.'''

tabela = [[0] * 2 for a in range (4)]
for numerolinhaa in range(2):
    for numerocoluna in range(4):
        #print("Valor Linha",numerocoluna + 1, "Coluna :" , numerolinha + 1)
       print("Valor linha %d coluna %d:" % (numerolinhaa + 1, numerocoluna + 1))
       tabela[numerocoluna][numerolinhaa] = int(input())
for coluna in range(2):
    for linha in range(4):
        print(tabela[linha][coluna], end=" ")
    print()