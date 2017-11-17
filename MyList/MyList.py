import sys,traceback

class MyList():
    def __init__(self,n):
        self.value = n

    def __del__(self):
        print(self.value)
        traceback.print_tb(limit=-10)

    def __set__(self):
        pass
