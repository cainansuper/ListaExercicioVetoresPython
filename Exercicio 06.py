vect = [int] * 5
soma = 0
mutiplicacao = 1

for i in range (len(vect)):
    vect[i] = int(input("Digite um número: "))

for i in range (len(vect)):
    soma += vect[i]
    mutiplicacao *= vect[i]

print("Soma: ", soma)
print("Mutiplicação: ", mutiplicacao)

print("Números: ")
for i in range(len(vect)):
    print(vect[i])