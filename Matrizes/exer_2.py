'''2)	Ler uma matriz A de duas dimensões com 7 linhas e 7 colunas.
Ao final apresentar o total de elementos pares existentes dentro da matriz.'''
npar = 0
tabela = [[0] * 7 for a in range (7)]
for numerocoluna in range(7):
    for numerolinhaa in range(7):
        #print("Valor Linha",numerocoluna + 1, "Coluna :" , numerolinha + 1)
       print("Valor Linha %d Coluna %d:" % (numerolinhaa + 1, numerocoluna + 1))
       tabela[numerocoluna][numerolinhaa] = int(input())
       if tabela[numerocoluna][numerolinhaa] % 2 == 0:
            npar = tabela[numerocoluna][numerolinhaa]
for coluna in range(7):
    for linha in range(7):
        print(tabela[linha][coluna], end=" ")
    print()
print("Os numeros pares são",npar)
