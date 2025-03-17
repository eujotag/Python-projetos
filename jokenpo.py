import random
from time import sleep

print("Vamos jogar Jokenpô")

options=["Pedra","Papel","Tesoura"]
maquina=random.choice(options)

options_dict={
    "1" : "Pedra",
    "2" : "Papel",
    "3" : "Tesoura"
}

player=input(
    "Faça sua escolha!\n"
    "1. Pedra\n"
    "2. Papel\n"
    "3. Tesoura\n"
    "Digite o número referente a sua escolha:").strip()

print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ!!!")
sleep(0.5)

player_choice = options_dict[player]


if player_choice == maquina:
    print("Empatamos.")
elif (player_choice == "Pedra" and maquina == "Tesoura") or \
     (player_choice == "Papel" and maquina == "Pedra") or\
     (player_choice == "Tesoura" and maquina == "Papel"):
     print("Você ganhou.")
else:
     print("Você perdeu man.")
print("Eu escolhi {} e você escolheu {}!".format(maquina,player_choice))
    