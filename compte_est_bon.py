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


def main():
    while True:
        print_numbers()

        if len(available_numbers) == 1:
            print("Il ne reste qu'un seul nombre.")
            break

        arret = input("Voulez-vous arrêter ? (o/n) : ").lower()
        if arret == 'o':
            break

        try:
            firs_number = int(input("Premier nombre : "))
            second_number = int(input("Deuxième nombre : "))

            temporary_list = available_numbers.copy()
            if firs_number in temporary_list:
                temporary_list.remove(firs_number)
            else:
                print("Le premier nombre n'est pas disponible.")
                continue

            if second_number in temporary_list:
                temporary_list.remove(second_number)
            else:
                print("Le deuxième nombre n'est pas disponible.")
                continue

        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        operation_choose = input("Opération (+, -, *, /) : ").strip()
        result = apply_operations(operation_choose, firs_number, second_number)

        if result is None:
            print("Opération invalide")
            continue

        print(f" {firs_number} {operation_choose} {second_number} = {result}")

        available_numbers.remove(firs_number)
        available_numbers.remove(second_number)
        available_numbers.append(result)

        if result == number_to_reach:
            print("\nLe compte est bon !")
            break


if __name__ == "__main__":
    main()