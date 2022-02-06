# (criando uma carteira digital que faz calculos)
# (O valor do dolar não é em tempo real)
# (Cotação atual R$5,59)

n = float(input("Quanto dinheiro você tem? \nR$"))
dolar1 = 5.27
#primeira
conversao = n / dolar1
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))

n = float (input ('Coloque mais um valor em reais! \nR$'))
dolar2 = 5.99
total = n / dolar2
print ('Vamos multiplicar os valores com R${} Saldo total é US${:.2f}.'.format(n, total))
s = conversao + total
print ('soma é US$',s)


