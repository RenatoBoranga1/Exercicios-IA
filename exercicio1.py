nome = input("Qual é o seu nome? ")

idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print(f"Olá, {nome}! Você é maior de idade.")
else:
    print(f"Olá, {nome}! Você é menor de idade.")