#private è una closure che restituisce un decoratore con la lista di campi privati groundata
def private(privatefields):
    def decorator(aclass):
        class wrapper:
            def __init__(self,*params):
                self.wrapped = aclass(*params)
                self.privates = privatefields

            def __getattribute__(self,attr):
                print("getattribute: "+attr)
                return super(wrapper,self).__getattribute__(attr)

            #getattr viene chiamato quando tutti gli altri metodi di accesso ai campi falliscono
            def __getattr__(self,attr):
                if(attr in self.privates):
                    raise AttributeError("Tentato accesso al campo privato: "+attr)
                else:
                    return getattr(self.wrapped,attr)

            def __setattr__(self,attr,value):
                if(attr in ['wrapped','privates']):
                    object.__setattr__(self,attr,value)
                elif(attr in self.privates):
                    raise AttributeError("Tentata modifica del campo privato: "+ attr)
                else:
                    setattr(self.wrapped,attr,value)
        return wrapper
    return decorator


@private(["count","setcount"])
class counter:
    def __init__(self,start):
        self.start = start
        self.count = start

    def setcount(self,value):
        self.count = value

    def inc(self):
        self.setcount(self.count+1)

    def reset(self):
        self.setcount(self.start)

    def getcount(self):
        return self.count
