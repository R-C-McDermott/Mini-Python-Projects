# Command line to-do list
#
# By Ryan C. McDermott
import os
import time
import colorama
from colorama import Fore, Style
colorama.init()


def return_linecount(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())


def print_to_do(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if "Checked" in line:
                print(Fore.GREEN + f"{i + 1}) " + line.strip("\n") + Style.RESET_ALL)
            else:
                print(Fore.RED + f"{i + 1}) " + line.strip("\n") + Style.RESET_ALL)


def append_to_do(filename):
    with open(filename, 'a') as f:
        while True:
            list_item = input("Add item to to-do list:\n>")
            f.write(list_item + "\n")
            while True:
                cont = input("Add another item? (y/n):\n>")
                if cont not in ["y", "n"]:
                    print("Invalid input")
                    continue
                else:
                    break
            if cont == "y":
                continue
            if cont == "n":
                break


def remove_item(filename):
    if return_linecount(filename) > 0:
        while True:
            print_to_do(filename)
            remove_index = int(input(f"Please choose item number between 1-{return_linecount(filename)} from above to remove item\n>"))
            if remove_index not in [x + 1 for x in range(return_linecount(filename))]:
                print("Invalid input, please try again")
                continue
            else:
                break
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as output:
            for line in lines:
                if line != lines[remove_index - 1]:
                    output.writelines(line)
    else:
        print("To-do list is empty!")


def checkoff_to_do(filename):
    if return_linecount(filename) > 0:
        while True:
            print_to_do(filename)
            check_index = int(input(f"Please choose item number between 1-{return_linecount(filename)} from above to check-off\n>"))
            if check_index not in [x + 1 for x in range(return_linecount(filename))]:
                print("Invalid input, please try again")
                continue
            else:
                break
        with open(filename, 'r') as f:
            lines = f.readlines()
        lines[check_index - 1] = lines[check_index - 1].strip("\n") + " - Checked\n"
        with open(filename, 'w') as output:
            output.writelines(lines)
    else:
        print("To-do list is empty!")


def append_routine(filename, routine_file):
    while True:
        routine_input = input("Would you like to append normal routine items? (y/n)\n>")
        if routine_input.strip().lower() not in ["y", "n"]:
            print("Invalid input, please try again")
            continue
        else:
            break
    if routine_input.strip().lower() == "y":
        with open(routine_file) as r:
            lines = r.readlines()
            with open(filename, "w") as f:
                for line in lines:
                    f.write(line)
                f.write("\n")
        print("Daily routine added!")
    if routine_input.strip().lower() == "n":
        print("No routine added!")


def user_loop():

    while True:
        user_input = input("What would you like to do? - Type 'help' for more information or press CRTL-C to exit\n>")
        if user_input.strip().lower() not in ["r", "a", "c", "d", "help", "exit"]:
            print("Invalid input, please try again")
            continue
        if user_input.strip().lower() == "help":
            print("Commands:\n"
                  "r - Read to-do list\n"
                  "a - add to to-do list\n"
                  "c - Check-off list item\n"
                  "d - Delete list item\n"
                  )
        else:
            break

    if user_input.lower() == "r":
        print_to_do(filename)
    if user_input.lower() == "a":
        append_to_do(filename)
    if user_input.lower() == "c":
        checkoff_to_do(filename)
    if user_input.lower() == "d":
        remove_item(filename)

    while True:
        prompt = input("Would you like to continue: (y/n)\n>")
        if prompt.strip().lower() not in ["y", "n"]:
            print("Invalid input, please try again")
            continue
        if prompt.strip().lower() == "y":
            user_loop()
        if prompt.strip().lower() == "n":
            print("Thank you! Goodbye!")
        break


def main():
    print("Hello, welcome to your to-do list!\n")

    # File creation/appending

    # Nested try/except blocks to avoid space-padding in ctime
    if os.path.isfile(filename) is True:
        try:
            _, month, day, _, year = time.ctime(os.path.getmtime(filename)).split(" ")
            _, today_month, today_day, _, today_year = time.ctime().split(" ")
        except ValueError:
            try:
                _, month, _, day, _, year = time.ctime(os.path.getmtime(filename)).split(" ")
                _, today_month, _, today_day, _, today_year = time.ctime().split(" ")
            except ValueError:
                try:
                    _, month, day, _, year = time.ctime(os.path.getmtime(filename)).split(" ")
                    _, today_month, _, today_day, _, today_year = time.ctime().split(" ")
                except ValueError:
                    _, month, _, day, _, year = time.ctime(os.path.getmtime(filename)).split(" ")
                    _, today_month, today_day, _, today_year = time.ctime().split(" ")
    if os.path.isfile(filename) is False:
        file = open(filename, "w+")
        print("New to-do list ready!\n")
        file.close()
        append_routine(filename, routine_file)
        user_loop()
    elif (day, month, year) != (today_day, today_month, today_year):
        file = open(filename, "w+")
        print("New to-do list ready!\n")
        file.close()
        append_routine(filename, routine_file)
        user_loop()
    else:
        print("Opening existing to-do list!\n")
        user_loop()


if __name__ == "__main__":
    filename = os.path.join(os.getcwd(), "todo.txt")
    routine_file = os.path.join(os.getcwd(), "routine.txt")
    main()



