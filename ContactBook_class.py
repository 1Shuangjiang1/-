from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, birthday, phone_number, email):
        self.name = name
        self.birthday = birthday
        self.phone_number = phone_number
        self.email = email

    @abstractmethod
    def get_info(self):
        pass

class WorkLife(Person):
    def __init__(self, name, birthday, phone_number, email):
        super().__init__(name, birthday, phone_number, email)

class PersonalLife(Person):
    def __init__(self, name, birthday, phone_number, email):
        super().__init__(name, birthday, phone_number, email)

class Classmate(PersonalLife):
    def __init__(self, name, birthday, phone_number, email, college, major):
        super().__init__(name, birthday, phone_number, email)
        self.college = college
        self.major = major

    def get_info(self):
        return f"Classmate: {self.name}, Birthday: {self.birthday}, Phone: {self.phone_number}, Email: {self.email}, College: {self.college}, Major: {self.major}"

class Teacher(WorkLife):
    def __init__(self, name, birthday, phone_number, email, college, title, ResearchDirection):
        super().__init__(name, birthday, phone_number, email)
        self.college = college
        self.title = title
        self.ResearchDirection = ResearchDirection

    def get_info(self):
        return f"Teacher: {self.name}, Birthday: {self.birthday}, Phone: {self.phone_number}, Email: {self.email}, College: {self.college}, Title: {self.title}, Research Direction: {self.ResearchDirection}"

class Colleague(WorkLife):
    def __init__(self, name, birthday, phone_number, email, company):
        super().__init__(name, birthday, phone_number, email)
        self.company = company

    def get_info(self):
        return f"Colleague: {self.name}, Birthday: {self.birthday}, Phone: {self.phone_number}, Email: {self.email}, Company: {self.company}"

class Friend(PersonalLife):
    def __init__(self, name, birthday, phone_number, email, how_met):
        super().__init__(name, birthday, phone_number, email)
        self.how_met = how_met

    def get_info(self):
        return f"Friend: {self.name}, Birthday: {self.birthday}, Phone: {self.phone_number}, Email: {self.email}, How Met: {self.how_met}"

class Relative(PersonalLife):
    def __init__(self, name, birthday, phone_number, email, relationship):
        super().__init__(name, birthday, phone_number, email)
        self.relationship = relationship

    def get_info(self):
        return f"Relative: {self.name}, Birthday: {self.birthday}, Phone: {self.phone_number}, Email: {self.email}, Relationship: {self.relationship}"
