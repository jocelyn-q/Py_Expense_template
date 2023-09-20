import csv
from PyInquirer import prompt

from user import load_users

user_names = []
users = load_users()
user_names = [user["SIGL"] for user in users]


SAVE_EXPENSE_FILE = "expense_report.csv"


def new_expense(*args):
    print(user_names)
    infos = prompt(expense_questions)

    ttt = {"payback": "['RDuval', 'PChojka', 'simon']"}

    # Extract the string value from the dictionary
    input_string = ttt["payback"]

    # Remove the leading and trailing square brackets and split the string by commas
    input_list = input_string.strip("[]").split(", ")

    # Remove any leading or trailing spaces from the elements and create the final list
    output_list = [element.strip("'") for element in input_list]

    print(output_list)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    expense = {
        "amount": infos["amount"],
        "label": infos["label"],
        "spender": infos["spender"],
        "payback": output_list,
    }
    save_to_csv_expense(expense)
    print("Expense Added !")
    return True


def save_to_csv_expense(expense):
    with open(SAVE_EXPENSE_FILE, "a", newline="") as csvfile:
        fieldnames = ["amount", "label", "spender", "payback"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(expense)


def load_expense_history():
    expenses = []
    with open(SAVE_EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)
    return expenses


def generate_status_report():
    expenses = load_expense_history()
    print(expenses)
    user_contributions = {}
    user_balances = {}

    for expense in expenses:
        amount = float(expense[0])
        spender = expense[2]
        involved_users = expense[3].split(", ")

        if spender not in user_contributions:
            user_contributions[spender] = 0
        user_contributions[spender] += amount

        for user in involved_users:
            if user not in user_contributions:
                user_contributions[user] = 0
            user_contributions[user] -= amount

    for user, contribution in user_contributions.items():
        user_balances[user] = contribution

    report = []
    for user1 in user_balances:
        for user2 in user_balances:
            if user1 != user2:
                balance = user_balances[user1] - user_balances[user2]
                if balance > 0:
                    report.append(f"{user1} owes {balance:.2f}€ to {user2}")

    return report
