#ler as notas separadamente
nota1 = float(input("Digite a primeira nota\n"))
nota2 = float(input("Digite a segunda nota\n"))
nota3 = float(input("Digite a terceira nota\n"))
nota4 = float(input("Digite a quarta nota\n"))

#calculo da média
media=((nota1*2)+(nota2*3)+(nota3*4)+(nota4*1))/10

#condicionais
if(media<7.0 and media>5.0):
    print("Media:", media)
    print("Aluno em exame!")
    exame = float(input("Digite a nota do exame:\n"))

    media = (media + exame)/2
    if(media>5.0):
        print("Media final:", media)
        print("Aprovado")
    elif(media<5.0):
        print("Media final:", media)
        print("Reprovado!")
elif(media>7.0):
    print("Media:", media)
    print("Aprovado")
elif(media<5.0):
    print("Media:", media)
    print("Reprovado!")
