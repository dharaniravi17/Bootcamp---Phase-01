import csv
import os
from datetime import datetime
BUDGET_FILE = "budget_data.csv"
def save_to_csv(income, expenses):
    with open(BUDGET_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Category", "Amount", "Date"])
        for source, amount in income.items():
            writer.writerow(["Income", source, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        for category, amount in expenses.items():
            writer.writerow(["Expense", category, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
def load_from_csv():
    income = {}
    expenses = {}

    if not os.path.exists(BUDGET_FILE):
        return income, expenses  

    with open(BUDGET_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  

        for row in reader:
            if row[0] == "Income":
                income[row[1]] = float(row[2])
            elif row[0] == "Expense":
                expenses[row[1]] = float(row[2])

    return income, expenses
def calculate_total_income(income_dict):
    return sum(income_dict.values())
def calculate_total_expenses(expenses_dict):
    return sum(expenses_dict.values())
def calculate_balance(income_total, expenses_total):
    return income_total - expenses_total
def get_user_data():
    income, expenses = load_from_csv()

    print("\n🔹 **Existing Budget Data Loaded!**")
    display_summary(income, expenses)
    n = int(input("\nHow many new income sources? (Enter 0 to skip): "))
    for _ in range(n):
        source = input("Enter income source: ")
        amount = float(input(f"Enter amount for {source}: ₹"))
        income[source] = amount
    m = int(input("\nHow many new expense categories? (Enter 0 to skip): "))
    for _ in range(m):
        category = input("Enter expense category: ")
        amount = float(input(f"Enter amount for {category}: ₹"))
        expenses[category] = amount

    save_to_csv(income, expenses)

    return income, expenses
def display_summary(income, expenses):
    total_income = calculate_total_income(income)
    total_expenses = calculate_total_expenses(expenses)
    balance = calculate_balance(total_income, total_expenses)

    print("\n **Budget Summary**")
    print(f" Total Income: ₹{total_income}")
    print(f" Total Expenses: ₹{total_expenses}")
    print(f" Balance: ₹{balance}")
def main():
    income, expenses = get_user_data()
    display_summary(income, expenses)

if __name__ == "__main__":
    main()
