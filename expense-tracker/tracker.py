# Expense Tracker - Installment 2: Talking to the User
# Author: Karl Daniel P. De Mesa
# Description: Displays the landing page, user input, and a summary of the two expenses.

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

# Computation of the Total Expenses
total = first_amount + second_amount
avg = total / 2

# Summary Display
print(f"\n{'-' * 40}")
print("SUMMARY")
print(f"\t-{first_item}: \t${first_amount:.2f}")
print(f"\t-{second_item}: \t${second_amount:.2f}")
print(f"Total Spent: \t\t${total:.2f}")
print(f"Average: \t\t${avg:.2f}")

# Footer
print("-" * 40)
print("Made By: Karl Daniel P. De Mesa  |  Installment 2\n\n")