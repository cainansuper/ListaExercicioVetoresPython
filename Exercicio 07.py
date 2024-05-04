idades = [int] * 5
alturas = [float] * 5

for i in range(len(idades)):
    print((i + 1), "ª pessoa: ")
    idades[i] = int(input("Digite a sua idade: "))
    alturas[i] = float(input("Digite a sua altura: "))
    print() 

somaIdade = 0
somaAltura = 0
maisNovo = idades[0]
maisVelho = idades[0]
maisAlto = alturas[0]
maisBaixo = alturas[0]
for i in range(len(idades)):
    somaIdade += idades[i]
    somaAltura += alturas[i]
    if idades[i] < maisNovo:
        maisNovo = idades[i]
    if idades[i] > maisVelho:
        maisVelho = idades[i]
    if alturas[i] < maisBaixo:
        maisBaixo = alturas[i]
    if alturas[i] > maisAlto:
        maisAlto = alturas[i]

mediaIdade = somaIdade/5
mediaAltura = somaAltura/5

print("Media das idades: ", mediaIdade)
print("Media das alturas: ", mediaAltura)
print("Mais novo: ", maisNovo)
print("Mais velho: ", maisVelho)
print("Mais alto: ", maisAlto)
print("Mais baixo: ", maisBaixo)
