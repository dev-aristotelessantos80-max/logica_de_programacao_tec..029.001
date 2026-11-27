# entrada de dados
nome = input("Informe o nome: ").strip().title()
nota1 = int(input("Informe a 1º nota: "))
nota2 = int(input("Informe a 2º nota: "))

# processamento de dados
media = (nota1+nota2)/2

# exibe a media
print(f"Média: {media}")

# estrutura de decisao
if media >= 7:
    print(f"{nome} esta aprovado.")
elif media >= 5:
    print(f"{nome} esta de recuperação.")
else:
    print(f"{nome} esta reprovado.")
