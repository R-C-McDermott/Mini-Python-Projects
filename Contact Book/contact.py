# Object file for contact

import datetime

class Contact(self, first_name, last_name, phone_number, dob, address):
    def __init__(self):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.dob = dob
        self.address = address

    def returnAge(self):
        day, month, year = self.dob.split("-")
        # datetime.date
        
def main():
    print(datetime.date)


if __name__ == '__main__':
    main()

