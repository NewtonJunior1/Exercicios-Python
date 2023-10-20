atend = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cep = [0] * 12
valor = [0] * 12
status = [0] * 12
num = 0
soma = 0
atmaior = 0
atmenor = 0
max = 0
min = 0
for i in range(12):
    num = num + 1
    print("Qual o cep do atendimento",num,"?")
    cep[i] = int(input())
    print("Qual o valor do atendimento",num,"?")
    valor[i] = int(input())
    print("Qual o status do atendimento",num,"?")
    status = str(input())
    if status == "REALIZADO" or "Realizado":
        soma = valor[i] + soma
    if i == 0:
        atmenor = valor[i]
    if valor[i] > atmaior:
        atmaior = valor[i]
        max = i
    if valor[i] < atmenor:
        atmenor = valor[i]
        min = i
    


print("listar atendimentos agendados = 1")
print("Calcular a soma do dinheiro recebido pelo chaveiro = 2")
print("Encontrar o cep mais caro e mais barato = 3")
print("Sair do programa = 4")
print("Digite a opção")
acao = int(input())

if acao == 1:
    print(atend)
    print("CEP",cep)
    print("Valores",valor)

if acao == 2:
    print(soma)

if acao == 3:
    print("O atendimento com o orçamento mais caro foi",atmaior)
    print("CEP=",cep[max])
    print("O atendimento com o orçamento mais barato foi",atmenor)
    print("CEP=",cep[min])

if acao == 4:
    print("Encerrando Programa")



