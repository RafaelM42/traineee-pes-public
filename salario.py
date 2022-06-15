rerun=1
while(rerun==1):    
    print("Opção 1: Reajuste de 10%")
    print("Opção 2: Reajuste de 15%")
    print("Opção 3: Reajuste de 20%")
    print("Opção 4: Outro valor")

    ##pega a opcao de reajuste
    opcao=float(input("Escolha a opção de reajuste.\n"))

    #reajuste definido pelo usuario
    if(opcao==4):
        reajuste=float(input("Digite o valor do reajuste sem a porcentagem:\n"))

    ##pega o salario do usuario
    sal=float(input("Digite aqui seu salário\n"))


    #Opções de cálculo
    if(opcao==1):
        sal = sal + (sal*10/100)
        print("Aumento de 10%")
    elif(opcao==2):
        sal = sal + (sal*15/100)
        print("Aumento de 15%")
    elif(opcao==3):
        sal = sal + (sal*20/100)
        print("Aumento de 20%")
    elif(opcao==4):
        sal = sal + (sal*reajuste/100)
        print("Aumento em percentual de", reajuste)

    ##Print do salário final após o reajuste
    print("-----------------------------------------")
    print("Seu salário reajustado será:", sal)
    print("-----------------------------------------")

    ##Easter Egg :)
    if(sal>10000):
        print("\nQue isso meu patrão(oa)!  B)")
    
    rerun=int(input("Gostaria de tentar novamente? Digite 1 caso queira.\n"))
    print("-----------------------------------------")
