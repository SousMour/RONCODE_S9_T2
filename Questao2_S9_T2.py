#Escreva um programa que leia um número inteiro menor que 1000 e 
# mostre por extenso a quantidade de centenas, dezenas e unidades do número lido, 
# observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. 
# Exemplos:
#521 = cinco centenas, duas dezenas e uma unidade.
#107 = uma centena e sete unidades.
#80 = oito dezenas.

import math
numero = int(input())
if numero <= 1000:
    centena = numero / 100
    centena2 = math.floor(float(centena))
    resto_centena = centena - centena2
    resto_multiplicado = resto_centena * 100

    dezena = resto_multiplicado / 10
    dezena2 = math.floor(float(dezena))
    unidade = dezena - dezena2
    unidade_certo = unidade * 10

    print("Centena(s): ", centena2)
    print("dezena(s): ", dezena2)
    print("Unidade(s): ", round(unidade_certo))

else:
    print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")