print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (total_bill + total_bill*(tip/100))/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")