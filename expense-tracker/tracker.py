# Expense Tracker - Installment 3: The Tracker Does Math
# Author: Karl Daniel P. De Mesa
# Description: Displays the landing page, user input, and a summary of the two expenses including tax.

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
second_item = input("Second Expense? ")
second_amount = float(input("Amount? "))
tax = input("Tax Rate %? ")
budget = float(input("Budget? "))

# Computations
subtotal = first_amount + second_amount
avg = subtotal / 2

tax_percent = float(tax) / 100
total = subtotal + (subtotal * tax_percent)
over_budget = total > budget

# Summary Display
print(f"\n{'-' * 40}")
print("SUMMARY")
print(f"\t-{first_item}:\t${first_amount:.1f}")
print(f"\t-{second_item}:\t\t${second_amount:.1f}")
print(f"Subtotal:\t\t${subtotal:.1f}")
print(f"Average:\t\t${avg:.2f}")
print(f"Tax ({float(tax)}%):\t\t${subtotal * tax_percent:.1f}")
print(f"Grand Total:\t\t${total:.1f}")
print(f"Over Budget? \t\t{over_budget}")
print(f"Left in Budget:\t\t${budget - total:.1f}")

# Footer
print("-" * 40)
print("Made By: Karl Daniel P. De Mesa  |  Installment 3\n\n")