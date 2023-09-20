import csv
from PyInquirer import prompt

from user import load_users

user_names = []
users = load_users()
user_names = [user["SIGL"] for user in users]


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
]

SAVE_EXPENSE_FILE = "expense_report.csv"


def new_expense(*args):
    print(user_names)
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    expense = {
        "amount": infos["amount"],
        "label": infos["label"],
        "spender": infos["spender"],
    }
    save_to_csv_expense(expense)
    print("Expense Added !")
    return True


def save_to_csv_expense(expense):
    with open(SAVE_EXPENSE_FILE, "a", newline="") as csvfile:
        fieldnames = ["amount", "label", "spender"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(expense)
