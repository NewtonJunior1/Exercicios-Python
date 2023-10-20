
'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um vetor.
Calcule e mostre a maior e a menor temperatura do ano e em que mês elas ocorreram
(mostrar o mês por extenso: 1- Janeiro, 2 – Fevereiro). Desconsidere empates.'''
lista = ["Janeiro", "Fevereiro", "março", "Abril", "maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
nummes = 0
x = 0
tempmin = 0
tempmax = 0
mesmenor = 0
mesmaior = 0
mes = [0] * 12
for i in range(12):
    nummes = nummes + 1
    print("Qual a temperatura media do mês", nummes, lista[x])
    x = x + 1
    mes[i] = int(input())
for i in range(12):
    if i == 0:
        tempmin = mes[i]
    if mes[i] > tempmax:
        tempmax = mes[i]
        mesmaior = i
    if mes[i] < tempmin:
        tempmin = mes[i]
        mesmenor = i
print("A temperatura maxima é de",tempmax,"e ela ocorre no mês de",lista[mesmaior])
print("A temperatura minima é de",tempmin,"e ela ocorre no mês de",lista[mesmenor])