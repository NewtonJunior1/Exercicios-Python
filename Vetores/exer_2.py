'''Faça um programa para corrigir provas de múltipla escolha com somatória.
Cada prova tem dez questões e cada questão vale 1 ponto.
O primeiro conjunto de dados a ser lido é o gabarito da prova.
Os outros dados serão os números dos alunos e sua respectivas respostas.
Existem 15 alunos matriculados. Calcule e mostre:
- Para cada aluno seu número e sua nota;
- A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
'''

gaba = [0] * 10
naluno = 0
nota = 0
aprovado = 0

for i in range(10):
        print("Qual o gabarito?")
        gaba[i] = int(input())

for i in range(15):
    naluno = naluno + 1
    print("Qual o nome do aluno?")
    nome = str(input())
    for j in range(10):
        print("Qual as respostas do aluno?")
        respostas = int(input())
        if respostas == gaba[j]:
            nota = nota + 1
        if nota >= 6:
            aprovado = aprovado + 1
    print("A nota do aluno",naluno, nome, "é", nota)

qntaprovado = (aprovado * 100) / 15
print("O percentual de aprovados é de", qntaprovado)
