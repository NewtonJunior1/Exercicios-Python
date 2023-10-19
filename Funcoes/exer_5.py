'''1.	Faça uma função que receba dois vetores A e B de dez elementos inteiros,
por parâmetro. O procedimento deve determinar e mostrar um vetor C que contenha
os elementos de A e B em ordem decrescente.'''

listaa = [0] * 10
listab = [0] * 10


def ordenadecrescente(la:list, lb:list):
    listac = [0] * 20
    for i in range(10):
        listac[i] = la[i]
    for i in range(10,20):
        listac[i] = lb[10-i]
    
    for i in range(0,19):
        for j in range(i+1,20):
            if listac[i] < listac[j]:
                listac[i], listac[j] = listac[j], listac[i]
    print(listac)

##codigo principal
for i in range(10):
    print("Digite um numero")
    listaa[i] = int(input())
for i in range(10):
    print("Digite um numero")
    listab[i] = int(input())
ordenadecrescente(listaa, listab)