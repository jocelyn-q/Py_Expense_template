import csv
from PyInquirer import prompt

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    },
]

SAVE_USER_FILE = "users.csv"


def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    user = {"name": infos["name"]}
    add_user_to_csv(user)
    print("User Added!")
    return True


def add_user_to_csv(user):
    with open(SAVE_USER_FILE, "a", newline="") as csvfile:
        fieldnames = ["name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(user)
