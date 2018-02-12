#Variaveis
palavra_secreta = 'bola'
tentativa = 5
tentativa = 5
vet=[]
letrasCertas = 0
print("Seja bem vindo ao jogo da forca")

print("\nPara poder comecar, vamos criar um login e senha\n")
login = input("Entre com seu nome de usuário: ")
print("\n...Muito bem!")

def entradaSenha():
        senha = input("\nEntre com uma boa senha: ")
        senha2 = input("\nApenas para podermos confirmar, digite sua senha novamente: ")
        return senha,senha2

def validacaoSenha():
    if senha==senha2:
        print("\nMuito bem, usuário criado com sucesso")
    else:
        print("\nOps!poderia tentar novamente? As senhas não bateram!")
        return False

while entradaSenha or validacaoSenha()==False:
    senha,senha2 = entradaSenha()
    validacaoSenha()
    if senha==senha2:
        break
print("\n\n\n...Que ótimo! Agora podemos dar prosseguimento ao nosso jogo!")
print("\n\n\n")

for i in range(len(palavra_secreta)):
    vet.append("_")

def verficaAcerto(tentativa,letrasCertas):
    while tentativa > 0:
        letra=input("entra com uma letra: ")
        for j in range(len(palavra_secreta)):
            if letra==palavra_secreta[j]:
                print("Letra correta")
                print("\nLetra encontrada no posição {}".format(j))
                vet[j]=letra
                letrasCertas+=1
                print(vet)
        if len(vet)==letrasCertas:
            print("Parabéns, você encontrou a palavra secreta")
            break
        tentativa-=1

verficaAcerto(tentativa,letrasCertas)
