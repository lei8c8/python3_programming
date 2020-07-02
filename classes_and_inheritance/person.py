CURRENT_YEAR = 2019

class Person():

    def __init__(self, name, year_born):
        self.name = name 
        self.year_born = year_born

    def getAge(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self):
        return "{} ({})".format(self.name, self.getAge())

class Student(Person):

    def __init__(self, name, year_born):
        super().__init__(name, year_born)
        self.knowledge = 0

    def study(self):
        self.knowledge += 1



if __name__ == '__main__':
    alice = Student("Alice Smith", 1990)
    alice.study()
    print(alice.knowledge)
    print(alice)
