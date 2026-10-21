def main():
    print("/// Bienvenue dans le programme de filtrage. ///\n")
    numbers = get_user_numbers()

    print("\nQuel mode de filtrage choisissez-vous ?")
    print("  1. Ne filtrer que les nombres pairs")
    print("  2. Ne filtrer que les nombres impairs")
    print("  3. Filtrer les nombres pairs et impairs")

    while True:
        choice = input("\nVotre choix (1, 2 ou 3) : \n\n").strip()
        if choice == "1":
            evens = filter_even_numbers(numbers)
            print(f"\n>> Nombres pairs ({len(evens)}) : {evens}")
            break
        elif choice == "2":
            odds = filter_odd_numbers(numbers)
            print(f"\n>> Nombres impairs ({len(odds)}) : {odds}")
            break
        elif choice == "3":
            evens = filter_even_numbers(numbers)
            odds = filter_odd_numbers(numbers)
            print(f"\n>> Nombres pairs ({len(evens)}) : {evens}")
            print(f">> Nombres impairs ({len(odds)}) : {odds}")
            break
        else:
            print(">> La saisie n'est pas correcte. Veuillez réessayer !\n")


def get_user_numbers():
    while True:
        user_input = input("Saisissez plusieurs nombres entiers séparés par des espaces. \n(Par exemple : 24 6 490 1 9 123)\n\n")

        if not user_input:
            print(">> La saisie ne doit pas être vide. Veuillez réessayer !\n")
            continue
        try:
            numbers = [int(val) for val in user_input.split()]
            return numbers
        except ValueError:
            print(">> La saisie n'est pas correcte. Veuillez réessayer !\n")


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]


main()