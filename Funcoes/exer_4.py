'''5)	Foi realizada uma pesquisa de algumas características físicas de cinco habitantes
de uma certa região. De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos
(A – Azuis ou C – Castanhos), cor dos cabelos (L – Louros, P – Pretos ou C – Castanhos) e idade.

a.	Faça uma função que leia esses dados em vetores. Determine, por meio de outra função,
a média de idade das pessoas com olhos castanhos e cabelos pretos. Mostre esse resultado no programa principal.

b.	Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.

c.	Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo
feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.
'''

sexo = str
olho = str
cabelo = str
idade = 0

def caracter(sexo: str, olho: str, cabelo: str, idade: int):
    cont = 0
    for i in range(5):
        cont += 1
        sexo = [0] * 5
        print("Qual o sexo da pessoa numero", cont)
        sexo[i] = input()
        olho = [0] * 5
        print("Qual a cor do olho da pessoa numero", cont)
        olho[i] = input()
        cabelo = [0] * 5
        print("Qual a cor do cabelo da pessoa numero", cont)
        cabelo[i] = input()
        idade = [0] * 5
        print("Qual a idade da pessoa numero", cont)
        idade[i] = input()

def calca(medidade):
    cont = 0
    for i in range(5):
        if olho[i] == "C" and cabelo[i] == "P":
            soma = soma + idade[i]
            cont += 1
    medidade = soma / cont

def idadem(maior):
    for i in range(5):
        maior = idade[i]
        if idade[i] > maior:
            idade[i] = maior






teste = caracter(sexo, olho, cabelo, idade)
print(teste)

media = calca
print("A media de idade é", media)

maioridade = idadem
print("A maior idade entre os 5 é", maioridade)

