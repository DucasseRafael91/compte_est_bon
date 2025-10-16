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
    print_numbers()
    apply_operations(apply_operations, available_numbers, plates)