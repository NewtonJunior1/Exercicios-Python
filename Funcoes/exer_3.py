'''4)	Faça uma função que receba cinco valores inteiros, e retorne o maior valor.
Faça uma segunda função que receba também cinco valores e retorne o menor deles.'''
def encontrarMaior(*numeros):
    omaior = 0
    for i in numeros:
        if i > omaior:
            omaior = i
    return omaior

def encontrarMenor(*numeros):
    omenor = numeros[0]
    for i in numeros:
        if i < omenor:
            omenor = i
    return omenor

guardar_resultado = encontrarMaior(1, 2, 3, 4, 5)
guardar_resultado1 = encontrarMenor(1, 2, 3, 4, 5)
print("o maior", guardar_resultado)
print("o menor", guardar_resultado1)