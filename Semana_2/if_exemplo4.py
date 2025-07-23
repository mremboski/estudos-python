meta_func = 10000
meta_loja = 250000
vendas_func = 5000
vendas_loja = 200000

if vendas_func > meta_loja and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_func
    print("O bonus do funcionario foi de {}".format(bonus))
else:
    print("O funcionario não ganhou bonus")
nota_func = 10
meta_nota = 9

if nota_func >= meta_nota or (vendas_func > meta_loja and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_func
    print("O Bonus do funcionario foi {}".format(bonus))
else: 
    print("O funcionario não ganhou bonus")