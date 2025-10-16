import random


grid_of_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                  6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
                  25, 50, 75, 100]

# Tirage
number_to_reach = random.randint(101, 999)
plates = random.sample(grid_of_values, 6)

# Liste des nombres disponibles : au départ, ce sont les 6 plaques
available_numbers = plates.copy()

print("Nombre à atteindre :", number_to_reach)

def print_numbers():
    print("🔢 Nombres disponibles :", available_numbers)

def apply_operations(op, a, b):
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
    while True:
        print_numbers()

        if len(available_numbers) == 1:
            print("Il ne reste qu'un seul nombre.")
            break

        arret = input("Voulez-vous arrêter ? (o/n) : ").lower()
        if arret == 'o':
            break

        try:
            a = int(input("Premier nombre : "))
            b = int(input("Deuxième nombre : "))

            if a == b and available_numbers.count(a) < 2:
                print("Ce nombre n'est disponible qu'une seule fois.")
                continue

            temporary_list = available_numbers.copy()
            if a in temporary_list:
                temporary_list.remove(a)
            else:
                print("Le premier nombre n'est pas disponible.")
                continue

            if b in temporary_list:
                temporary_list.remove(b)
            else:
                print("Le deuxième nombre n'est pas disponible.")
                continue

        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        operation_choose = input("Opération (+, -, *, /) : ").strip()
        result = apply_operations(operation_choose, a, b)

        if result is None:
            print("Opération invalide")
            continue

        print(f" {a} {operation_choose} {b} = {result}")

        available_numbers.remove(a)
        available_numbers.remove(b)
        available_numbers.append(result)

        if result == number_to_reach:
            print("\nLe compte est bon !")
            break