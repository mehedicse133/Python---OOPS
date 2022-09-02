# python inheritance 

class person:

    def __init__(self, name, age, phone=None):
        self.__name = name
        self.age = age
        self.phone = phone

    def details(self):
        return f'I am {self.__name} and age {self.age}'

    def getname(self):
        return self.__name

    def setname(self,newname):
        self.__name= newname   



class student(person):       # Inherite parent class person
    
    def __init__(self,name,age,email,dept):
        super().__init__(name, age)
        self.email = email
        self.dept = dept

    def details(self):
        return f'I am {self.getname()} and age {self.age} and email {self.email}' 



if __name__ == "__main__":
    s = student("Mehedi",11,'m@gamil.com','cse') 
    s.setname('amam')   
    print(s.details())  
    print(s.getname())  


    # class teacher(person):
    #     def __init__(self,):
            

    # p1 = person('Mehedi',10)
    # p2 = person("Amam",30)
    # for i in [p1,p2]:
    #     print(i.details())