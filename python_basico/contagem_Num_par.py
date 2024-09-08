"""2. Contagem de Números Pares
Descrição: Peça ao usuário para inserir um número inteiro positivo. Conte e exiba a quantidade de números pares de 1 até o número fornecido."""

numero = int(input("Digite Numero: "))
cont = 0
i=1
while i <= numero:
    if i % 2 == 0:
        cont +=1
    i +=1
print(f" exsite {cont} numero pares")   

