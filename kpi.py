# Desafio do dia: Cálculo de Bônus com Entrada do Usuário
# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.
#O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# Receber o nome do usuario
nome = str(input("Digite seu nome: "))
salario = float(input("Digite o valor do seu salario: "))
bonus = float(input("Digite o valor do bônus: "))
print(f"Olá {nome}, o seu valor bônus foi de {1000 + ( salario * bonus)}")