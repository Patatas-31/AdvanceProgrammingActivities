# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Karl Daniel P. De Mesa
# Description: Shows a banner, asks the setup questions once, then repeats a
# menu until the user chooses Exit. Tracks the count and subtotal of expenses.

# Banner
print("=" * 40)
print("\t  EXPENSE TRACKER")
print("\tKnow Your Expenses")
print("=" * 40)

# User Input
name = input("\nWhat's Your Name? ")
tax_percent = input("Tax Rate %? ")
budget = float(input("Your Budget? "))
print(f"Welcome, {name}!")

choice = ""
count = 0
subtotal = 0

# Menu
while choice != "4":
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses (coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("\tHuge expense - are you sure?")
        elif amount > 100:
            print("\tBig expense.")
        elif amount > 50:
            print("\tModerate expense.")
        else:
            print("\tSmall expense.")
    elif choice == "2":
        print("\tComing soon: the tracker can't remember each item yet.")
    elif choice == "3":
        tax = float(tax_percent) / 100
        total = subtotal + (subtotal * tax)
        over_budget = total - budget
        ninety_percent_budget = budget * 0.9
        print(f"Expenses:\t\t{count}")
        print(f"Subtotal:\t\t${subtotal:.1f}")
        print(f"Tax ({float(tax_percent)}%):\t\t${subtotal * tax:.1f}")
        print(f"Grand total:\t\t${total:.1f}")
        if total > budget:
            print(f"Over budget by ${over_budget:.1f}!")
        elif total > ninety_percent_budget:
            print(f"Careful: only ${abs(over_budget):.1f} left.")
        else:
            print(f"Within budget. ${abs(over_budget):.1f} left.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
    else:
        print("\tPlease choose 1, 2, 3 or 4.")


# Footer
print("-" * 40)
print("Made by: Karl Daniel P. De Mesa  |  Installment 5")
print("=" * 40)