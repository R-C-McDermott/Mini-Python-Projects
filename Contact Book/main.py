# File for writing to CSV

from contact import Contact
import datetime
import csv
from csv import DictWriter
import os.path

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

def addDOB():
    try:
        birth = input("Please enter date of birth (DD-MM-YYYY): ")
        birth = datetime.datetime.strptime(birth, '%d-%m-%Y').date()
    except ValueError:
        print("Invalid input, please try again.")
        addDOB()
    else:
        d, m, y = birth.strftime('%d-%m-%Y').split("-")
        return d + "-" + m + "-" + y

def main():
    initial_input = input(">")
    initial_input.lower()
    if initial_input not in ['y', 'n']:
        print("invalid input, please try again.")
        main()
    if initial_input == 'n':
        print("Goodbye!")
    if initial_input == 'y':
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

if __name__ == '__main__':
    csv_name = "contacts.csv"
    if os.path.isfile(csv_name) is True:
        pass
    else:
        initiate_csv(csv_name)

    print("Hello! would you like to add to your contacts? (y/n)")
    main()