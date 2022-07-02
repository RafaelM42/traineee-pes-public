hora1 = int(input("Digite a hora de início"))
minuto1 = int(input("Digite o minuto de início"))

hora2 = int(input("Digite a hora de término"))
minuto2 = int(input("Digite o minuto de término"))

minuto1 = minuto1 * 5
minuto2 = minuto2 * 5

if(minuto2>minuto1):
    total_minutos = (minuto2-minuto1)
elif(minuto2<minuto1):
    total_minutos = (minuto2+60)-minuto1


if(hora2>hora1):
    total_horas = (hora2-hora1)
elif(hora2<hora1):
    total_horas = (hora2+24)-hora1

print("O jogo durou", total_horas, "hora(s) e", total_minutos, "minutos")
