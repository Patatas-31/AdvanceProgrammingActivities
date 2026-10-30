# Expense Tracker - Installment 4: The Tracker Makes Decisions
# Author: Karl Daniel P. De Mesa
# Description: Displays the landing page, user input, and a summary of the two expenses. 
# The system displays a message to the user if they are over budget, within budget, or close to the budget limit.

# Banner
print("=" * 40)
print("\t  EXPENSE TRACKER")
print("\tKnow Your Expenses")
print("=" * 40)

# Menu
print("\nMAIN MENU")
print("\t[1] Add Expense\t\t\t(coming soon)")
print("\t[2] View Expenses\t\t(coming soon)")
print("\t[3] Show Total Expenses\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

# User Input
name = input("\nWhat's Your Name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

first_item = input("First Expense? ")
first_amount = float(input("Amount? "))
if first_amount > 200:
    print("\tHuge expense - are you sure?")
elif first_amount > 100:
    print("\tBig expense.")
elif first_amount > 50:
    print("\tModerate expense.")
elif first_amount <= 50 and first_amount >= 0:
    print("\tSmall expense.")
else:
    print("\tInvalid input. Please enter a valid amount.")

second_item = input("Second Expense? ")
second_amount = float(input("Amount? "))
if second_amount > 200:
    print("\tHuge expense - are you sure?")
elif second_amount > 100:
    print("\tBig expense.")
elif second_amount > 50:
    print("\tModerate expense.")
elif second_amount <= 50 and second_amount >= 0:
    print("\tSmall expense.")
else:
    print("\tInvalid input. Please enter a valid amount.")

if first_amount > 100 and second_amount > 100:
    print("Two big expenses in a row - slow down!")

tax = input("Tax Rate %? ")
budget = float(input("Your Budget? "))

# Computations
subtotal = first_amount + second_amount
avg = subtotal / 2

tax_percent = float(tax) / 100
total = subtotal + (subtotal * tax_percent)
over_budget = total - budget
ninety_percent_budget = budget * 0.9

# Summary Display
print(f"\n{'-' * 40}")
print("SUMMARY")
print(f"\t-{first_item}:\t\t${first_amount:.1f}")
print(f"\t-{second_item}:\t\t${second_amount:.1f}")
print(f"Subtotal:\t\t${subtotal:.1f}")
print(f"Average:\t\t${avg:.2f}")
print(f"Tax ({float(tax)}%):\t\t${subtotal * tax_percent:.1f}")
print(f"Grand Total:\t\t${total:.1f}")
if total > budget:
    print(f"Over budget by ${over_budget:.1f}!")
elif total > ninety_percent_budget:
    print(f"Careful: only ${abs(over_budget):.1f} left.")
else:
    print(f"Within budget. ${abs(over_budget):.1f} left.")

# Footer
print("-" * 40)
print("Made by: Karl Daniel P. De Mesa  |  Installment 4\n\n")