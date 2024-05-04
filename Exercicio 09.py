temperaturaMedia = [float] * 12
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
somaMedia = 0

for i in range(len(temperaturaMedia)):
    temperaturaMedia[i] = float(input(f"Digite a temperatura media de {meses[i]}: "))
    somaMedia += temperaturaMedia[i]

mediaAnual = somaMedia/12
print("Media Anual = {:.2f}".format(mediaAnual))
print("Meses que passaram a temperatura media anual: ")

for i in range(len(temperaturaMedia)):
    if temperaturaMedia[i] > mediaAnual:
        print((i + 1), "-", meses[i], ":", "{:.2f}".format(temperaturaMedia[i]))