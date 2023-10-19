'''2)	Faça uma função que transforme e mostre segundos em:
 horas, minutos e segundos. Todas as variáveis devem ser passadas como parâmetro, não havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s
'''

def convseg(qntseg:int):
    qnthoras = int(qntseg / 3600)
    sobraseg = qntseg % 3600
    minutos = int(sobraseg / 60)
    segundos = sobraseg % 60
    print(f"horas:  {qnthoras}")
    print(f"minutos:  {minutos}")
    print(f"segundos: {segundos}")
    

print("Digite uma quantidade de segundos")
seg = int(input())
convseg(seg)