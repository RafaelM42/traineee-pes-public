## Rafael Mello, Marcelo Silveira e Luiz Gabriel Lima.
## Plotar a sequência de fibonacci, na qual cada "sessão" tem uma cor.

##Importar a biblioteca de plotagem gráfica.
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

##Criar uma lista para armazenar os termos da sequência
termos=[]

##Criar uma lista para armazenar a posição de cada termo na sequência
pos=[]

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

    ##Colocar os termos unitários na lista
    termos.append(1)
    termos.append(1)
    pos.append(1)
    pos.append(2)
    
## Laço de repetição para printar demais números até 
## o que foi determinado pelo usuário.
while (count <= n):
    termo=ultimo + penultimo
    penultimo=ultimo
    ultimo=termo

    pos.append(count)
    termos.append(termo)

    count+=1
    print(termo)

##Comandos para plotar o gráfico

ax.plot(pos, termos)    #chama a plotagem (x,y)
plt.xlabel('Posição dos termos')    #Título do eixo x
plt.ylabel('Termo da sequência')    #Título do eixo y
plt.title('Fibonacci')  #Título do gráfico
plt.show()  #Plota o gráfico em uma imagem.
