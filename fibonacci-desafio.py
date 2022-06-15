## Rafael Mello, Marcelo Silveira e Luiz Gabriel Lima.
## Plotar a sequência de fibonacci, na qual cada "sessão" tem uma cor.

##Importar a biblioteca de plotagem gráfica.
import matplotlib
from matplotlib import pyplot as plt

## Pegar o número de termos a ser encontrado
n=int(input('Termo que deseja encontrar:'))
## Os primeiros termos da sequência
ultimo=1
penultimo=1

##Caso dos dois primeiros termos
if(n==1) or (n==2):
    print("1")
else:
    ##Caso para demais números
    count=3
    #printar os "1" da sequência.
    print('1')
    print('1')

## Laço de repetição para printar demais números até 
## o que foi determinado pelo usuário.
while (count <= n):
    termo=ultimo + penultimo
    penultimo=ultimo
    ultimo=termo

    count+=1
    print(termo)
