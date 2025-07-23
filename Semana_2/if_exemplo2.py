meta = 0.05
taxa = 0
rendimento = float(input("Qual o valor do seu rendimento?"))

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print("A taxa cobrada será de {}".format(taxa))
    else:
        taxa = 0.02
        print("A taxa cobra será de {}".format(taxa))
else:
    taxa = 0
    print("Como o rendimento foi abaixo do esperado não haverá taxa!")