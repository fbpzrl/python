print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

print()
numero_secreto = 42

chute = int(input("Digite o seu número: "))

print()

if (chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")

print"Fim do Jogo!"