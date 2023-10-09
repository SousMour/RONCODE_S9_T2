#Um sacolão está vendendo frutas com a seguinte tabela de preços:

#Até 5Kg Acima de 5Kg
#Morango R$ 2,50 por Kg R$ 2,20 por Kg
#Maça R$ 1,80 por Kg R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda umdesconto de 10% sobre este total. 
# Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def preco_frutas(morango, maca):
  if morango or maca <= 5:
    valor_morango = morango * 2,5
    valor_maca= maca * 1,8
    valor_total_1 = valor_morango + valor_maca
    if morango or maca > 5:
      valor_morango = morango * 2,2
      valor_maca= maca * 1,5
      valor_total_2 = valor_morango + valor_maca
      if morango + maca > 8  or  valor_total_1 > 25 or valor_total_2 > 25:
        desconto_1= (morango + maca)* 0,9
        print(desconto_1)
        desconto_2= valor_total_1 *0,9
        print(desconto_2)
        desconto_3 = valor_total_2 * 0,9
        print(desconto_3)
      print(valor_total_2)
    print(valor_total_1)
  
maca= int(input())
morango= int(input())
resultado = preco_frutas(morango,maca)
