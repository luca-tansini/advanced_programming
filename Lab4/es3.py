class pascaltriangleiterator():
    def __init__(self):
        self.index = 0
        self.rows = []

    def __iter__(self):
        self.__init__()
        return self

    def __next__(self):
        if(self.index == 0):
            row = [1]
        else:
            row = []
            for i in range(self.index+1):
                if(i-1 >= 0):
                    a = self.rows[self.index-1][i-1]
                else:
                    a = 0
                if(i<self.index):
                    b = self.rows[self.index-1][i]
                else:
                    b = 0
                row += [a+b]
        self.rows += [row]
        self.index += 1
        return row.__iter__()

def printnpascalrows(n):
    pascal = pascaltriangleiterator()
    for i in range(n):
        print((n-1-i)*"  ",end="")
        for e in next(pascal):
            print("{:2d}".format(e),end="  ")
        print()

printnpascalrows(5)
printnpascalrows(8)
printnpascalrows(9)
