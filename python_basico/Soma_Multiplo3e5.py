"""Soma de Números Múltiplos de 3 e 5 Descrição: Peça ao usuário um número inteiro positivo e calcule a soma de todos os números múltiplos de 3 e 5 até esse número."""
Num = int(input("Digite Numero : "))
soma =0
for i in range(Num+1):
    if i%3 ==0 or i%5 ==0 :
        soma = soma + i 

print(f"A soma dos Multiplo de 3 e 5 do Numero {Num} é {soma}")

    