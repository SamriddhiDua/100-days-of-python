print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

choice1 = input('Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('Type "wait" or "swim": ').lower()

    if choice2 == "wait":
        choice3 = input('Choose a door: "red", "blue", "yellow": ').lower()

        if choice3 == "yellow":
            print(" You win!")
        elif choice3 == "red":
            print(" Game Over")
        elif choice3 == "blue":
            print(" Game Over")
        else:
            print("Invalid choice. Game Over")

    else:
        print(" Game Over")

elif choice1 == "right":
    print(" Game Over")

else:
    print("Invalid input. Game Over")
