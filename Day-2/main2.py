print("Welcome to Tip Calculator!")

bill = float(input("What was the bill? \n$"))
tip = int(input("how much tip would you like to give? \n10, 12, or 15? "))
people = int(input("How many people to split the bill\n"))

total_bill = bill + tip
per_person = total_bill/people

print(f"Each person should pay: ${per_person}")