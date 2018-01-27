class ProvaMeta(type):
    def __call__(cls,*arg,**kargs):
        print("sovrascritto metodo __call__ di type!")
        return type.__call__(cls,*arg,**kargs)

    def __new__(meta,classname,supers,classdict):
        print("sovrascritto metodo __new__ di type!")
        return type.__new__(meta,classname,supers,classdict)

class ProvaClass(metaclass=ProvaMeta):
    def __init__(self,param):
        self.value = param

    def getvalue(self):
        return self.value

p = ProvaClass(42)
