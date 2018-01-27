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

class Counter(type):
    def __new__(meta,classname,superclasses,classdict):
        classdict['counter'] = 0
        return type.__new__(meta,classname,superclasses,classdict)

    def __call__(cls,*arg,**kargs):
        cls.counter += 1
        print("la classe "+cls.__name__+" è stata inizializzata "+str(cls.counter)+" volte")
        return type.__call__(cls,*arg,**kargs)

class PersonWithCounter(Person,metaclass=Counter): pass

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

class Spell(type):
    def __call__(cls,*arg,**kargs):
        arg += (7.5,)
        return type.__call__(Worker,*arg,**kargs)

class PersonWithSpell(Person,metaclass=Spell): pass

def MultiTriggeredMethod(method):
    def wrapped(*args,**kargs):
        if(wrapped.count < 2):
            print("metodo "+method.__name__+" non ancora sbloccato")
            wrapped.count+=1
        else:
            return method(*args,**kargs)
    wrapped.count = 0
    return wrapped

class MetaDecorator(type):
    def __new__(meta,classname,superclasses,classdict):
        for k,i in classdict.items():
            if (type(i).__name__ == 'function'):
                classdict[k] = MultiTriggeredMethod(i)
        return type.__new__(meta,classname,superclasses,classdict)

class PersonWithMetaDecorator(metaclass=MetaDecorator):
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
        return super(PersonWithMetaDecorator,self).__repr__() + " (" + self.getname() + " " + self.getlastname() + " nato il " + self.getbirthday() + ")"
