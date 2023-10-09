#Escreva um programa que leia um número e exiba o dia correspondente da semana. 
# (1-domingo, 2-segunda-feira, 3-terça-feira etc.), 
# se digitar outro valor deve aparecer “valor inválido”.

def dia_semana(n):
    if n == 1:
        print('domingo')
    elif n == 2:
        print('segunda-feira') 
    elif n == 3:
        print('terça-feira')
    elif n == 4:
        print('quarta-feira')
    elif n == 5:
        print('quinta-feira')
    elif n == 6:
        print('sexta-feira')
    elif n == 7:
        print('sábado')
    else:
        print('valor inválido')
dia= int(input())
resultado= dia_semana(dia)