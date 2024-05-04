vectX = [int] * 6
for i in range(len(vectX)):
    vectX[i] = int(input("Digite um valor: "))

vectY = [int] * 6

for o in range(len(vectY)):
    vectY[o] = vectX[i]
    i -= 1

print("Vetor normal: ", vectX)
print("Vetor invertido: ", vectY)