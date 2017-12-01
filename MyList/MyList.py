import inspect

class MyList():
    def __init__(self,n):
        self.value = n

    def __del__(self):
        for f in inspect.getouterframes(inspect.currentframe()):
            print(f,end="\n\n")
            frame = f[0]
            print("*****f_code*****\n")
            print(frame.f_code, end="\n\n")
            print("*****f_locals*****\n")
            print(frame.f_locals, end="\n\n")
            frame.f_locals['l']=42
            #print("*****f_globals*****\n")
            #print(frame.f_globals, end="\n\n")
            print("*"*80+"\n")
