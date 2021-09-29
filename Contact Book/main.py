# File for writing to CSV

from contact import Contact
import datetime
import csv
from csv import DictWriter
import os.path
import pandas as pd

def initiate_csv(filename):
    headers = ["NAME", "PHONE NUMBER", "DATE OF BIRTH", "ADDRESS", "POSTCODE"]
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def append_csv(filename, contact_dictionary):
    headers = ["NAME", "PHONE NUMBER", "DATE OF BIRTH", "ADDRESS", "POSTCODE"]
    with open(filename, 'a') as file:
        dict_writer_object = DictWriter(file, fieldnames=headers)
        dict_writer_object.writerow(contact_dictionary)
        file.close()

def createDataframe(filename):
    df = pd.read_csv(filename)
    df.set_index("NAME", inplace=True)
    return df


def accessContact(df):
    name_input = input("Please enter the full name of the contact you require details of:\n>").lower().title()
    if name_input not in df.index:
        print(f"No contact named {name_input} exists")
        accessContact()
    else:
        print(df.loc[name_input])

def addDOB():
    try:
        birth = input("Please enter date of birth (DD-MM-YYYY): ")
        birth = datetime.datetime.strptime(birth, '%d-%m-%Y').date()
    except ValueError:
        print("Invalid input, please try again.")
        addDOB()
    else:
        d, m, y = birth.strftime('%d-%m-%Y').split("-")
        return d + "/" + m + "/" + y

def continueInput():
    continue_input = input(">").lower()
    if continue_input not in ['y', 'n']:
        print("Invalid input, please try again.")
        continueInput()
    if continue_input == 'y':
        return True
    if continue_input == 'n':
        return False

def addReturnContact(csv_name):
    run = True
    while run:
        df = createDataframe(csv_name)
        print("Would you like to add or return a contact? (a/r) - Press CTRL-C to exit")
        initial_input = input(">").lower()
        if initial_input not in ['a', 'r']:
            print("invalid input, please try again.")
            addReturnContact()
        if initial_input == 'r':
            accessContact(df)
            print("Would you like to add or return another contact? (y/n):")
            run = continueInput()
        if initial_input == 'a':
            fn = input("Please enter first name: ")
            ln = input("Please enter last name: ")
            pn = str(input("Please enter phone number: "))
            birth = addDOB()
            hn = input("Please enter house number: ")
            sn = input("Please enter street name: ")
            cn = input("Please enter city: ")
            pc = input("Please enter postcode: ")

            new_contact = Contact(fn, ln, pn, birth, hn, sn, cn, pc)
            new_row_data = new_contact.create_dictionary()
            append_csv(csv_name, new_row_data)
            print("Contact added!")
            print("Would you like to add or return another contact? (y/n):")
            run = continueInput()


def main():
    csv_name = "contacts.csv"
    if os.path.isfile(csv_name) is True:
        pass
    else:
        initiate_csv(csv_name)

    addReturnContact(csv_name)

if __name__ == '__main__':
    main()