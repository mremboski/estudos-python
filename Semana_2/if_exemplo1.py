meta = 51000
qtd_vendas = 65300

if qtd_vendas > meta:
    print("Parabéns a meta de vendas foi batida, efetuamos a venda de {} unidades." .format(meta))


""" EXEMPLO com else """

meta_vendas = 50000
qtde_vendas = 50000

if qtde_vendas >= meta_vendas:
    print("Parabéns a meta de vendas foi batida, efetuamos a venda de {} unidades." .format(meta_vendas))
else:
    print("Infelizmente você não bateu a meta de vendas esse mês!")