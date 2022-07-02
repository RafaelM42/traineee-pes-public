#Usando o split para recolher várias variáveis 
codigo1, quant1, valor1 = input().split(" ")

codigo2, quant2, valor2 = input().split(" ")

#Calculando o valor de cada
total1 = (int(quant1)*float(valor1))
total2 = (int(quant2)*float(valor2))

#soma
total_geral = total1 + total2

print("Valor a pagar:R$ %f", total_geral)