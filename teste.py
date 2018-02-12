palavra = "bala"
vet_ico = []
index = 0
letrasCertas=0
tentativa=5

print(len(palavra), len(vet_ico))

for i in range(len(palavra)):
    vet_ico.append("-")

while tentativa>0:
    letra = input("entre com a letra: ")
    for j in range(len(palavra)):
        if letra == palavra[j]:
            letrasCertas+=1
            print("letra encontrada na posição {}".format(j))
            vet_ico[j] = letra
            print(vet_ico)
    if len(vet_ico)==letrasCertas:
        print("Parabéns, Palavra completa")
        break
    tentativa-=1
print(len(palavra), len(vet_ico))
