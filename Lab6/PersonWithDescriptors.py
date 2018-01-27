class Person:
    def __init__(self,name,last,birthday):
        self.__name = name
        self.__lastname = last
        self.__birthday = birthday

    def getname(self):
        return self.__name

    def setname(self,newname):
        self.__name = newname

    def getlastname(self):
        return self.__lastname

    def setlastname(self,newlast):
        self.__lastname = newlast

    def getbirthday(self):
        return self.__birthday

    def __repr__(self):
        return super(Person,self).__repr__() + " (" + self.getname() + " " + self.getlastname() + " nato il " + self.getbirthday() + ")"

class grade_average_descriptor:

    def __get__(self,instance,type):
        tot = 0
        for mark in instance.lectures.values():
            tot += mark
        return tot/len(instance.lectures)

    def __set__(self,instance,value):
        print("Pippo")

class Student(Person):
    def __init__(self,name,last,birthday,lectures):
        super(Student,self).__init__(name,last,birthday)
        self.lectures = lectures

    grade_average = grade_average_descriptor()

class salary_descriptor:
    def __init__(self,hours):
        self.hours = hours

    def __get__(self,instance,type):
        return instance.pay_per_hour * self.hours
    def __set__(self,instance,value):
        instance.pay_per_hour = value/self.hours

class Worker(Person):
    def __init__(self,name,last,birthday,payph):
        super(Worker,self).__init__(name,last,birthday)
        self.pay_per_hour = payph

    day_salary = salary_descriptor(8)
    week_salary = salary_descriptor(8*5)
    month_salary = salary_descriptor(8*5*4)
    year_salary = salary_descriptor(8*5*4*12)
