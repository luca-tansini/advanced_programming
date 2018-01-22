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

class Student(Person):
    def __init__(self,name,last,birthday,lectures):
        super(Student,self).__init__(name,last,birthday)
        self.__lectures = lectures

    def __get_grade_average(self):
        tot = 0
        for mark in self.__lectures.values():
            tot += mark
        return tot/len(self.__lectures)

    grade_average = property(__get_grade_average)

class Worker(Person):
    def __init__(self,name,last,birthday,payph):
        super(Worker,self).__init__(name,last,birthday)
        self.__pay_per_hour = payph

    def __get_day_salary(self):
        return self.__pay_per_hour * 8

    def __set_day_salary(self,daysal):
        self.__pay_per_hour = daysal/8

    day_salary = property(__get_day_salary,__set_day_salary)

    def __get_week_salary(self):
        return self.day_salary * 5

    def __set_week_salary(self,weeksal):
        self.day_salary = weeksal/5

    week_salary = property(__get_week_salary,__set_week_salary)

    def __get_month_salary(self):
        return self.week_salary * 4

    def __set_month_salary(self,monthsal):
        self.week_salary = monthsal/4

    month_salary = property(__get_month_salary,__set_month_salary)

import datetime,re

class Wizard(Person):
    def __init__(self,name,last,birthday):
        self.__name = name
        self.__lastname = last
        m = re.match("(?P<day>[0-9]{1,2})-(?P<month>[0-9]{1,2})-(?P<year>[0-9]{1,5})",birthday)
        self.__birthday = datetime.date(int(m.group('year')),int(m.group('month')),int(m.group('day')))

    def getbirthday(self):
        return self.__birthday.strftime("%d-%m-%Y")

    def __get_age(self):
        return (datetime.date.today() - self.__birthday).days

    def __set_age(self,ageindays):
        self.__birthday = datetime.date.today() - datetime.timedelta(ageindays)

    age = property(__get_age,__set_age)
