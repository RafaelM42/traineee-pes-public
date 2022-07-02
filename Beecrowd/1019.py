#declaração do tempo
tempo = int(input("Digite o tempo em segundos"))

#condicional para haver minutos
if(tempo>60):
    minutos = tempo//60 #divisão
    segundos = tempo%60 #resto
elif(tempo<=60):    #caso para não haver minutos
    horas = 0
    minutos = 0

#condicional para haver horas
if(minutos>60):
    horas = minutos//60
    minutos = minutos%60
elif(minutos<=60):  #não há horas
    horas = 0

print(horas, ":", minutos, ":", segundos)