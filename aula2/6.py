# Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais estão corretas.

usuario = 'admin'
senha = '12345'

loginusuario = input("Digite seu login: ")
loginsenha = input("Digite seu senha: ")

if loginusuario == usuario and loginsenha == senha:
    print("Seu usúario e senha estão corretos.")
else:
    print(f"Usuário ou senha incorreto.")
