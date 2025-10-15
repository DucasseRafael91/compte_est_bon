import random

nombre = random.randint(101, 999)

reparties = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
             6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
             25, 50, 75, 100]

# Tirer 6 nombres au hasard depuis la liste (respecte les doublons disponibles)
tirage = random.sample(reparties, 6)

print("Nombre cible :", nombre)
print("Nombres tirés :", tirage)
