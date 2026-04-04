# Tip Calculator

print("Welcome to the tip calculator!\n")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10, 12, 15): "))
people = int(input("How many people to split the bill? "))

if people <= 0:
    print("Number of people must be greater than 0")
    exit()

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

print(f"\nEach person should pay: ${bill_per_person:.2f}")

