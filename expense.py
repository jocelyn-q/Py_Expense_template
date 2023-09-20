import csv
from PyInquirer import prompt

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
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },
]

EXPENSES_FILE = "expense_report.csv"


def new_expense(*args):
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
    with open(EXPENSES_FILE, "a", newline="") as csvfile:
        fieldnames = ["amount", "label", "spender"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Écrivez les données de la dépense dans le fichier CSV
        writer.writerow(expense)
