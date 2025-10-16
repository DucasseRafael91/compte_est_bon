#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Liste de valeurs possibles pour les plaques (certaines valeurs apparaissent deux fois)
grid_of_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                  6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
                  25, 50, 75, 100]

# Nombre cible à atteindre (entre 101 et 999)
number_to_reach = random.randint(101, 999)

# Tirage de 6 plaques au hasard parmi les valeurs
plates = random.sample(grid_of_values, 6)

# Copie des plaques disponibles (utile pour le jeu manuel)
available_numbers = plates.copy()

# Fonction qui applique toutes les opérations possibles entre deux nombres
def apply_operations(a, b):
    results = []

    # Addition
    results.append((a + b, f"{a} + {b} = {a + b}"))

    # Multiplication
    results.append((a * b, f"{a} * {b} = {a * b}"))

    # Soustraction (on garde seulement les résultats positifs ou nuls)
    if a > b:
        results.append((a - b, f"{a} - {b} = {a - b}"))
    elif b > a:
        results.append((b - a, f"{b} - {a} = {b - a}"))

    # Division entière si elle est exacte
    if b != 0 and a % b == 0:
        results.append((a // b, f"{a} / {b} = {a // b}"))
    if a != 0 and b % a == 0:
        results.append((b // a, f"{b} / {a} = {b // a}"))

    return results

# Fonction récursive de backtracking pour résoudre le problème
def solve(current_numbers, operation_history):
    # Si le nombre cible est atteint, on retourne l'historique des opérations
    if number_to_reach in current_numbers:
        return operation_history

    # Si un seul nombre reste et ce n'est pas la cible, il n'y a pas de solution possible
    if len(current_numbers) == 1:
        return None

    # On essaye toutes les paires possibles de nombres
    for index_a in range(len(current_numbers)):
        for index_b in range(len(current_numbers)):
            if index_a == index_b:
                continue  # On évite de prendre deux fois le même nombre

            number_a = current_numbers[index_a]
            number_b = current_numbers[index_b]

            # On crée une nouvelle liste sans les deux nombres sélectionnés
            remaining_numbers = [
                current_numbers[k]
                for k in range(len(current_numbers))
                if k != index_a and k != index_b
            ]

            # On applique toutes les opérations valides entre number_a et number_b
            for operation_result, operation_description in apply_operations(number_a, number_b):
                # On met à jour l'historique avec cette nouvelle opération
                updated_history = operation_history + [operation_description]

                # Appel récursif avec la nouvelle liste de nombres
                solution = solve(remaining_numbers + [operation_result], updated_history)

                # Si une solution a été trouvée, on la retourne immédiatement
                if solution:
                    return solution

    # Si aucune solution n'a été trouvée dans cette branche de récursion
    return None

# Mode de jeu manuel : le joueur choisit ses opérations
def play_manually():
    available = plates.copy()

    while True:
        print("Nombre à atteindre :", number_to_reach)
        print("Nombres disponibles :", available)

        if len(available) == 1:
            print("Il ne reste qu'un seul nombre.")
            break

        arret = input("Voulez-vous arrêter ? (o/n) : ").lower()
        if arret == 'o':
            break

        try:
            first_number = int(input("Premier nombre : "))
            operation = input("Opération (+, -, *, /) : ").strip()
            second_number = int(input("Deuxième nombre : "))

            # Vérification que les deux nombres sont bien disponibles
            temp_list = available.copy()
            if first_number in temp_list:
                temp_list.remove(first_number)
            else:
                print("Le premier nombre n'est pas disponible.")
                continue

            if second_number in temp_list:
                temp_list.remove(second_number)
            else:
                print("Le deuxième nombre n'est pas disponible.")
                continue

        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        # Application de l'opération choisie
        result = None
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            if second_number != 0 and first_number % second_number == 0:
                result = first_number // second_number
            else:
                print("Division invalide.")
                continue
        else:
            print("Opération non reconnue.")
            continue

        print(f"{first_number} {operation} {second_number} = {result}")

        # Mise à jour de la liste : on retire les deux nombres utilisés et on ajoute le résultat
        available.remove(first_number)
        available.remove(second_number)
        available.append(result)

        # Vérification si le compte est bon
        if result == number_to_reach:
            print("Le compte est bon !")
            break

# Fonction principale qui lance le jeu
def main():
    print("Nombre à atteindre :", number_to_reach)
    print("Plaques :", plates)

    # Choix du joueur : jeu manuel ou solution automatique
    choice = input("Souhaitez-vous jouer manuellement ? (o/n) : ").lower()

    if choice == 'o':
        play_manually()
    else:
        solution = solve(plates, [])

        if solution:
            print("\nSolution trouvée :")
            for step in solution:
                print(step)
            print("Le compte est bon.")
        else:
            print("Aucune solution exacte trouvée.")

# Lancement du programme
if __name__ == "__main__":
    main()
