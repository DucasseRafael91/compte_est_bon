import random


grid_of_values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                  6, 6, 7, 7, 8, 8, 9, 9, 10, 10,
                  25, 50, 75, 100]

# Tirage
number_to_reach = random.randint(101, 999)
plates = random.sample(grid_of_values, 6)

available_numbers = plates.copy()



def print_numbers():
    print("🔢 Nombres disponibles :", available_numbers)

def apply_operations(operation, first_number, second_number):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number != 0 and first_number % second_number == 0:
            return first_number // second_number
        else:
            return None
    else:
        return None


def main():
    while True:
        print("Nombre à atteindre :", number_to_reach)
        print_numbers()

        if len(available_numbers) == 1:
            print("Il ne reste qu'un seul nombre.")
            break

        arret = input("Voulez-vous arrêter ? (o/n) : ").lower()
        if arret == 'o':
            break

        try:
            firs_number = int(input("Premier nombre : "))
            operation_choose = input("Opération (+, -, *, /) : ").strip()
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