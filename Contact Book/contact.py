# Object file for contact

class Contact:
    def __init__(self, first_name, last_name, phone_number, dob, house_number, street_name, city, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.dob = dob
        self.house_number = house_number
        self.street_name = street_name
        self.city = city
        self.postcode = postcode

    def create_dictionary(self):
        contact_dictionary = {
             "NAME": self.first_name.lower().title() + " " + self.last_name.lower().title(),
             "PHONE NUMBER": "(+44)" + self.phone_number,
             "DATE OF BIRTH": self.dob,
             "ADDRESS": self.house_number + " " + self.street_name.lower().title() + ", " + self.city.lower().title(),
             "POSTCODE": self.postcode
        }

        return contact_dictionary
