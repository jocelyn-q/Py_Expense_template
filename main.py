from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions, new_expense
from status import generate_status_report
from user import add_user


def ask_option():
    main_option = {
        "type": "list",
        "name": "main_options",
        "message": "Expense Tracker v0.1",
        "choices": ["New Expense", "Show Status", "New User", "Leave"],
    }
    option = prompt(main_option)
    if (option["main_options"]) == "New Expense":
        new_expense()
        ask_option()
    if (option["main_options"]) == "New User":
        add_user()
        ask_option()
    if (option["main_options"]) == "Show Status":
        report = generate_status_report()
        if report:
            print("Status Report:")
            for line in report:
                print(line)
        else:
            print("No expenses found.")
        ask_option()
    if (option["main_options"]) == "Leave":
        return


def main():
    ask_option()


main()
