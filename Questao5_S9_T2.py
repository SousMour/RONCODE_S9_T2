#Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima ?"
#b) "Esteve no local do crime ?"
#c) "Mora perto da vítima ?"
#d) "Devia para a vítima ?"
#e) "Já trabalhou com a vítima ?"
#Considere “S” para sim ou “N” para não. 
# O programa deve emitir uma classificação sobre a participação da pessoano crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4
#como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def contador_s(resposta):
    contador = 0
    resposta = str(resposta).lower()
    if(resposta == 's'):
        contador+=1
    return contador

def crime(contador):
    status = ''
    if(contador < 2):
        status = 'Inocente'
    elif(contador == 2):
        status = 'Suspeito'
    elif(contador == 3 or contador == 4):
        status = 'Cúmplice'
    elif(contador == 5):
        status = 'Assassino'
    else:
        raise ValueError('Entrada inválida')   

    return status    



contador = 0
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resposta = input().strip()
contador += contador_s(resposta)
resultado = crime(contador)
print(f'{resultado}')
    
