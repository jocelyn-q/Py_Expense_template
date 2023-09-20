import csv
from PyInquirer import prompt

from user import load_users

user_names = []
users = load_users()
user_names = [user["SIGL"] for user in users]

payback_choices = [
    {
        "name": user,
        "value": user,
        "checked": True,
    }
    for user in user_names
]

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": user_names,
    },
    {
        "type": "checkbox",
        "name": "payback",
        "message": "New Expense - Paybacks: ",
        "choices": payback_choices,
    },
]

SAVE_EXPENSE_FILE = "expense_report.csv"


def new_expense(*args):
    infos = prompt(expense_questions)

    expense = {
        "amount": infos["amount"],
        "label": infos["label"],
        "spender": infos["spender"],
        "payback": ",".join(infos["payback"]),
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
