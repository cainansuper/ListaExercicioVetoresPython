real = [float] * 10
quadrado = [float] * 10

for i in range(len(real)):
    real[i] = float(input("Digite um valor: "))
    quadrado[i] = real[i] * real[i]

print("Conjunto real: ", real)
print("Conjunto do quadrado do conjunto real: ", quadrado)