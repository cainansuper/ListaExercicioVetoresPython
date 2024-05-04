n = int(input("Qual o número de vendedores? "))
vendedores = [str] * n
vendasBrutas = [float] * n
comissao = [float] * n

for i in range(len(vendedores)):
    vendedores[i] = str(input(f"Digite o nome do {i + 1}º vendedor: "))
    vendasBrutas[i] = float(input(f"Digite o valor da venda bruta do {i + 1}º vendedor: "))
    comissao[i] = 200 + (0.09 * vendasBrutas[i])

for o in range(len(comissao)):
    if comissao[o] < 299:
        if comissao[o] <= 299:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 200 - 299")
    if comissao[o] > 299 and comissao[o] <= 399:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 299 - 399")
    if comissao[o] > 399 and comissao[o] <= 499:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 399 - 499")
    if comissao[o] > 499 and comissao[o] <= 599:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 499 - 599")
    if comissao[o] > 599 and comissao[o] <= 699:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 599 - 699")
    if comissao[o] > 699 and comissao[o] <= 799:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 699 - 799")
    if comissao[o] > 799 and comissao[o] <= 899:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 799 - 899")
    if comissao[o] > 899 and comissao[o] <= 999:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 899 - 999")
    if comissao[o] > 999:
            print(f"{o + 1}º vendedor: ", vendedores[o], ", vendas Brutas: ", vendasBrutas[o], ", comissão: ", comissao[o], ", intervalo: 1000 - ...")
    print()