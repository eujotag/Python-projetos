import random
from time import sleep  # Importando as funções "random.choice" e "sleep".

print("Vamos jogar Jokenpô")

# Lista com as opções disponíveis no jogo
options = ["Pedra", "Papel", "Tesoura"]

# Escolha aleatória da máquina
maquina = random.choice(options)

# Dicionário para mapear números às escolhas
options_dict = {
    "1": "Pedra",
    "2": "Papel",
    "3": "Tesoura"
}

# Solicitando a escolha do jogador
player = input(
    "Faça sua escolha!\n"
    "1. Pedra\n"
    "2. Papel\n"
    "3. Tesoura\n"
    "Digite o número referente à sua escolha: "
).strip()

# Animação para criar suspense
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ!!!")
sleep(0.5)

# Obtendo a escolha do jogador a partir do dicionário
player_choice = options_dict[player]

# Verificando o resultado do jogo
if player_choice == maquina:
    print("Empatamos.")
elif (player_choice == "Pedra" and maquina == "Tesoura") or \
     (player_choice == "Papel" and maquina == "Pedra") or \
     (player_choice == "Tesoura" and maquina == "Papel"):
    print("Você ganhou.")
else:
    print("Você perdeu man.")

# Exibindo as escolhas
print("Eu escolhi {} e você escolheu {}!".format(maquina, player_choice))

# Exemplo de saída:
# Vamos jogar Jokenpô
# Faça sua escolha!
# 1. Pedra
# 2. Papel
# 3. Tesoura
# Digite o número referente à sua escolha: 1
# JO...
# KEN...
# PÔ!!!
# Eu escolhi Tesoura e você escolheu Pedra!
# Você ganhou.
    
