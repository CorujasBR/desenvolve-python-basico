comprimento = int(input("favor entra com o valor do comprimento do terreno: "))
largura  = int(input("favor entra com o valor da largura do terreno: "))
area_2 = comprimento * largura
valor_metro_quadrado = float(input("entre com o valor do metro quadrado: "))
preco_final  = area_2 * valor_metro_quadrado
print(f"O terreno poussui cerca de ", valor_metro_quadrado, "m2","o valor do metro quadrado eh: ",preco_final, "reais" )