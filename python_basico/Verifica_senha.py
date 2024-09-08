"""Validação de Senha Descrição: Solicite ao usuário uma senha e verifique se ela tem pelo menos 8 caracteres, contém uma letra maiúscula e um número. Informe se a senha é válida ou não.

Exemplo de saída:

python
Copiar código
Digite a senha: Segura123
Senha válida!"""

senha = input("Digite senha : ")
maiuscula = False
numero = False

# Verifica se a senha tem pelo menos 8 caracteres
if len(senha) < 8:
    print("Senha ivalido , Tem que ter pelo menos 8 digitos ")
else:
    # Itera sobre cada caractere da senha
    for caract in senha:
       if caract.isupper():  # verificar se tem caractere maiuscula
           maiuscula = True
       if caract.isdigit():  # verificar se tem um numero
            numero = True
            
     # Verifica se a senha contém ao menos uma letra maiúscula e um número       
    if maiuscula and numero:
        print("Senha valido!!!")
    else:
        print("Senha inválida: deve conter pelo menos uma letra maiúscula e um número.")
            
           
           