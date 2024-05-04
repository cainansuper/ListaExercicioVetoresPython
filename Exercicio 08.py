vectX = [int] * 10

for i in range(len(vectX)):
    vectX[i] = int(input("Digite um elemento: "))

vectY = [int] * 10

for o in range(len(vectY)):
    vectY[o] = vectX[i]
    i -= 1

print("Vetor X: ", vectX)
print()
print("Vetor Y: ", vectY)