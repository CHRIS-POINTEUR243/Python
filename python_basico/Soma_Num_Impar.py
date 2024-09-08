"""4. Soma de Números Ímpares
Descrição: Peça ao usuário para inserir um número inteiro positivo. Calcule e exiba a soma de todos os números ímpares de 1 até o número fornecido."""

num = int (input("Digite numero : "))
i = 1
soma = 0
while i <= num :
    if i %2 !=0 :
        soma = soma + i
    i +=1
print(f"Soma entra os numero impare de 1 ate {num} é {soma}")