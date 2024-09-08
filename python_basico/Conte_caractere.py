"""5. Contagem de Caracteres Específicos
Descrição: Solicite ao usuário que insira uma string e um caractere específico. Conte e exiba o número de vezes que o caractere aparece na string."""

palavra = input("Digite uma palavra : ")
caractere = input("Digite um caractere especifico : ")
cont =0
for letra in palavra :
    if caractere in letra :
        cont +=1
print(f"o caractere aprece {cont} vezes ")
