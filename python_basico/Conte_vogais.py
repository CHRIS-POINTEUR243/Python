"""2. Contagem de Vogais (Intermediário)
Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.
"""
palavra = input("Digite palavra: ")
vogais = "aeioueAEIOUE"
cont_vogais = 0
for letra in palavra: 
    if letra in vogais:
        cont_vogais +=1
print(f"existe : {cont_vogais} vogais")


