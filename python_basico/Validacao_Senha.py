"""Validação de Senha Descrição: Solicite ao usuário uma senha e verifique se ela tem pelo menos 8 caracteres, contém uma letra maiúscula e um número. Informe se a senha é válida ou não."""
senha = input("Digite a senha : ")
majuscula_tem = False
numero_tem = False

if len(senha) < 8:
    print("Senha deve ter pelo menos 8 digitos ")
else:
    for caractere in senha:
        if caractere[i].isupper():
            majuscula_tem = True
