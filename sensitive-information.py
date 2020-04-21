# Create a class to represent a patient of a doctor's office. The Patient class will 
# accept the following information during initialization
# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name 
# should not be exposed as properties at all, but instead expose a calculated 
# property of full_name. Address should have a getter and setter.

class Patient():

    def __init__(self, social, birthdate, insurance, first_name, last_name, address):
        self.__social = social
        self.__birthdate = birthdate
        self.__insurance = insurance
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def social(self):
        try:
            return self.__social
        except AttributeError:
            return 0

    @property
    def birthdate(self):
        try:
            return self.__birthdate
        except AttributeError:
            return 0

    @property
    def insurance(self):
        try:
            return self.__insurance
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__addresss = new_address
        else:
            raise TypeError("Please provide a string value for the address")

cashew = Patient("097-23-100", "08/13/92", "7001294103", "Daniela", "Agnoletti", "500 Infinity Way")

# This should not change the state of the object
#cashew.social = "838-31-2256"

# Neither should this
#cashew.birthdate = "01-30-90"

# But printing either of them should work
print(cashew.social)   # "097-23-1003"

# These two statements should output nothing
#print(cashew.first_name)
#print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"