# Define a Python class named Student. This class will have 5 properties.

class Student():
    
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort
        
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_first):
        if type(new_first) is str:
            self.__first_name = new_first
        else:
            raise TypeError("Only use a string value for first_name please")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0
    
    @last_name.setter
    def last_name(self, new_last):
        if type(new_last) is str:
            self.__last_name = new_last
        else:
            raise TypeError("Only use a string value for last_name please")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Only use an integer value for age please")

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            0

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError("Only use an integer value for cohort please")

    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return 0

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort}"