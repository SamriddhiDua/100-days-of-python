import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(nr_letters, nr_numbers, nr_symbols):
    password_list = []

    # Add random letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    # Add random symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Add random numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Shuffle the characters
    random.shuffle(password_list)

    # Convert list to string
    password = "".join(password_list)

    return password


print("Welcome to the Password Generator!\n")

while True:
    try:
        nr_letters = int(input("How many letters would you like? "))
        nr_numbers = int(input("How many numbers would you like? "))
        nr_symbols = int(input("How many symbols would you like? "))

        if nr_letters < 0 or nr_numbers < 0 or nr_symbols < 0:
            print("Please enter positive numbers only.\n")
            continue

        password = generate_password(nr_letters, nr_numbers, nr_symbols)

        print("\n Your generated password is:")
        print(password)

    except ValueError:
        print("Please enter valid numbers only.\n")
        continue

    again = input("\nGenerate another password? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye")
        break
