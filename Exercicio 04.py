vect = [float] * 8
soma = 0

for i in range(len(vect)):
    vect[i] = float(input("Digite um valor: "))

x = int(input("Digite uma posição x do vetor: "))
y = int(input("Digite uma posição y do vetor: "))

for i in range(len(vect)):
    if vect[i] == x:
        soma += vect[i]
    if vect[i] == y:
        soma += vect[i]


print("Resultado = ", soma)