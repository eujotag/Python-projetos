#aprendendo a ultilizar o loops do for
n1 = int(input("Digite um número para ver sua tabuada:")) #espera a entrada de um número inteiro definido pela variável n1.
for r in range(1,11): #percorre os valores de 1 a 10, o range(1, 11) gera números de 1 até 10.
    print("{} x {:2} = {}".format(n1,r,n1*r)) #Mostra a seguinte formatação n1 x r = n1*r ; loop de 1 até 10.


#Exemplo de saída:
#Digite um número para ver sua tabuada: 5
#5 x  1 = 5
#5 x  2 = 10
#5 x  3 = 15
#5 x  4 = 20
#5 x  5 = 25
#5 x  6 = 30
#5 x  7 = 35
#5 x  8 = 40
#5 x  9 = 45
#5 x 10 = 50
