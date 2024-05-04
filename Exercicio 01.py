vect = [1, 2, 4, 16, 32, 64, -128]

maior = 0
menor = 0

for i in range(len(vect)):
    if vect[i] > maior:
        maior = vect[i]
    if vect[i] < menor:
        menor = vect[i]

print("Maior valor: ", maior)
print("Menor valor: ", menor)