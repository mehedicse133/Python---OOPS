# Define a class
class Person:

    # class attributes
    person = []
    total = 0

    # constractor method
    def __init__(self) -> None:

        # instance attributes
        self.name = None
        self.__age = None
        self.__adult = None
        self.person.append(self)

    # gretter and public method
    def get_name(self):
        return self.name

    # setter and private mehtod
    def __set_name(self, new_name):
        self.name = new_name
    
    # instance methods
    def add(self, name, age):
        self.name = name
        self.__age = age
        self.adult = self.__is_adult(age)
    
    
    # property decorator
    @property
    def details(self):
        return f"My name is {self.name}, I am {self.adult}."

    # static method
    @staticmethod
    def __is_adult(age):
        if age >= 18:
            return "Adult"
        return "Teen age"

    # class method
    @classmethod
    def num_of_person(cls):
        return len(cls.person)

if __name__ == "__main__":
    p = Person()
    p.add("mehedi",17)
  




    # p1 = Person()
    # p1.add("Mehedi", "")
    # print(p1.adult)


    # person_list = Person.person
    # for i in person_list:
    #     print(i.details)


    # Person.num_of_person()

    # p1 = Person("Mehedi", 10)
    # p2 = Person("Mehedi", 15)
    # p3 = Person("Mehedi", 14)
    # p4 = Person("Mehedi", 24)
    # print(Person.num_of_person())
    # print(Person.is_adult(p1.age))

    # personlist = [p1, p2, p3, p4]
    # for i in personlist:
    #     print(i.deatils)


