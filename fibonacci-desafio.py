
n=int(input('Termo que deseja encontrar:'))
ultimo=1
penultimo=1

if(n==1) or (n==2):
    print("1")
else:
    count=3
    #printar os "1" da sequência.
    print('1')
    print('1')

while (count <= n):
    termo=ultimo + penultimo
    penultimo=ultimo
    ultimo=termo

    count+=1
    print(termo)
