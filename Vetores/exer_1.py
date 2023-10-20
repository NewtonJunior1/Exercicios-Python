'''Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os
códigos de dez contas e os seus respectivos saldos. Os códigos devem ser armazenados
em um vetor de números inteiros (não pode haver mais que uma conta com o mesmo código)
e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá ser cadastrado
na mesma posição do código. Por exemplo, se a conta 504 for armazenada na quinta posição do vetor
de saldos. Depois de fazer a leitura dos valores, mostrar o seguinte menu na tela:
'''
x = 0
cont = 0
conta = [0] * 10
saldo = [0] * 10
soma = 0
for i in range(10):
    cont = cont + 1
    print("conta numero", cont )
    repete = True
    while repete:
        print("Qual a conta à ser consultada?")
        novonumero = int(input())
        for j in range(10):
            if novonumero == conta[j]:
                print("Conta duplicada, digite outra.")
                repete = True
                break
            if j == 9:
                repete = False
                print("Conta inserida")
                conta[i] = novonumero
    print("Qual o saldo da conta", conta[i])
    saldo[i] = int(input())
    soma = saldo[i] + soma
print("Deposito = 1, saque = 2, consultar ativo bancario = 3 ou finalizar programa = 4")
acao = int(input())
if acao == 1:
    print("Qual o codigo da conta?")
    codi = int(input())
    for i in range(10):
        if conta[i] == codi:
            print("Qual o valor do deposito?")
            dep = int(input())
            saldo[i] = saldo[i] + dep
            print(saldo[i])
            break
        if conta[i] != codi:
            print("conta não encontrada")
            break

if acao == 2:
    print("Qual o codigo da conta?")
    codi2 = int(input())
    for i in range(10):
        if conta[i] == codi2:
            print("Qual o valor do saque?")
            saq = int(input())
            if saq > saldo[i]:
                saldo[i] = saldo[i] - saq
                print(saldo[i])
                break
        if codi2 != conta[i]:
            print("conta não encontrada")
            break

if acao == 3:
    print("O ativo bancario é de",soma)

if acao == 4:
    print("Finalizar programa!!!!!!!!!")

        
    
'''
i.	Efetuar depósito
ii.	Efetuar saque
iii.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
iv.	Finalizar o programa
Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado.
Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu.
Se a conta existir, atualizar o seu saldo.
############################################################################################
Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada, mostrar a
mensagem Conta não encontrada e voltar ao menu. Se a conta existir, verificar se o seu saldo é suficiente para cobrir o saque.
(Estamos supondo que a conta não pode ficar com o saldo negativo). Se o saldo for suficiente, realizar o saque e voltar ao menu.
Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.
Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor, voltar ao menu.
O programa só termina quando for digitada a opção 4 – Finalizar o programa.'''