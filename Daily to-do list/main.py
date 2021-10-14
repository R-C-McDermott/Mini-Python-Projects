# Command line to-do list
#
# By Ryan C. McDermott
import os
import time

def return_linecount(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

def print_to_do(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line.strip("\n"))

def append_to_do(filename):
    count = (return_linecount(filename) + 1)
    with open(filename, 'a') as f:
        while True:
            list_item = input("Add item to to-do list:\n>")
            f.write(str(count) + ") " + list_item + "\n")
            while True:
                cont = input("Add another item? (y/n):\n>")
                if cont not in ["y", "n"]:
                    print("Invalid input")
                    continue
                else:
                    break
            if cont == "y":
                count += 1
                continue
            if cont == "n":
                break

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

def user_loop():

    while True:
        user_input = input("What would you like to do? - Type 'help' for more information or press CRTL-C to exit\n>")
        if user_input.strip().lower() not in ["r", "a", "c", "help", "exit"]:
            print("Invalid input, please try again")
            continue
        if user_input.strip().lower() == "help":
            print("Commands:\n"
                  "r - Read to-do list\n"
                  "a - add to to-do list\n"
                  "c - Check-off list item\n"
                  )
        else:
            break

    if user_input.lower() == "r":
        print_to_do(filename)
    if user_input.lower() == "a":
        append_to_do(filename)
    if user_input.lower() == "c":
        checkoff_to_do(filename)


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

    if os.path.isfile(filename) is True:
        _, month, day, _, year = time.ctime(os.path.getctime(filename)).split(" ")
        _, today_month, today_day, _, today_year = time.ctime().split(" ")
    if os.path.isfile(filename) is False:
        file = open(filename, "w+")
        print("New to-do list ready!\n")
        file.close()
        user_loop()
    elif (day, month, year) != (today_day, today_month, today_year):
        file = open(filename, "w+")
        print("New to-do list ready!\n")
        file.close()
        user_loop()
    else:
        print("Opening existing to-do list!\n")
        user_loop()

if __name__ == "__main__":
    filename = os.path.join(os.getcwd(), "todo.txt")
    main()

