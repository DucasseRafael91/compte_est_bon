import random


reparties = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
             6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
             25, 50, 75, 100]

# Tirage
cible = random.randint(101, 999)
plaques = random.sample(reparties, 6)

# Liste des nombres disponibles : au départ, ce sont les 6 plaques
nombres_disponibles = plaques.copy()

print("Nombre à atteindre :", cible)

def afficher_nombres():
    print("🔢 Nombres disponibles :", nombres_disponibles)

def appliquer_operation(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0 and a % b == 0:
            return a // b
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    afficher_nombres()
    appliquer_operation(appliquer_operation, cible, plaques)