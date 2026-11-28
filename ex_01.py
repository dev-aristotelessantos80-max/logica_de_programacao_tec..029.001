gasolina = float(input("Informe o valor da gasolina: ").replace(',','.'))
etanol = float(input("Informe o valor do etanol: ").replace(',','.'))

if etanol <= gasolina*0.75:
    print("Melhor abastecer com Etanol")
else:
    print("Melhor abastecer com Gasolina.")


