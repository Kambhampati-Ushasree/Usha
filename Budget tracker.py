import json

# Initialize budget data
budget = {
    "income": 0,
    "expenses": [],
}

# Load existing data from a JSON file if available
try:
    with open("budget_data.json", "r") as file:
        budget = json.load(file)
except FileNotFoundError:
    pass

def save_budget_data():
    # Save budget data to a JSON file
    with open("budget_data.json", "w") as file:
        json.dump(budget, file)

def show_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def add_income():
    income = float(input("Enter income amount: "))
    budget["income"] += income
    save_budget_data()
    print(f"Income of ${income:.2f} added successfully.")

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    budget["expenses"].append({"category": category, "amount": amount})
    budget["income"] -= amount
    save_budget_data()
    print(f"Expense of ${amount:.2f} in '{category}' category added successfully.")

def view_budget():
    print("\nBudget Summary:")
    print(f"Income: ${budget['income']:.2f}")
    print("Expenses:")
    for expense in budget["expenses"]:
        print(f"- {expense['category']}: ${expense['amount']:.2f}")
    remaining_budget = budget["income"]
    for expense in budget["expenses"]:
        remaining_budget -= expense["amount"]
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def view_expense_analysis():
    expense_analysis = {}
    for expense in budget["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_analysis:
            expense_analysis[category] += amount
        else:
            expense_analysis[category] = amount
    print("\nExpense Analysis:")
    for category, amount in expense_analysis.items():
        print(f"{category}: ${amount:.2f}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_budget()
        elif choice == "4":
            view_expense_analysis()
        elif choice == "5":
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
