class sorted_dict_iter():
    def __init__(self,sorted_dict):
        self.list = sorted_dict.keys()
        self.index = 0
        self.max = len(self.list)-1

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if(self.index > self.max): raise StopIteration
        ret = self.list[self.index]
        self.index+=1
        return ret


class SortedDict(dict):
    #La mia soluzione sarebbe sortare il dizionario ogni volta che qualcuno vuole vederlo

    def __iter__(self):
       return sorted_dict_iter(self)

    def keys(self):
        return sorted(super(SortedDict,self).keys())

    def items(self):
        return [(k,self.get(k)) for k in self.keys()]

    def values(self):
        return [self.get(k) for k in self.keys()]

    def __getitem__(self,key):
        print("Vorresti l'elemento associato a {0}?".format(key))
        return super(SortedDict, self).__getitem__(key)

    def __setitem__(self,key,value):
        print("Vorresti impostare l'elemento associato a {0}?".format(key))
        return super(SortedDict, self).__setitem__(key,value)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        s = "{"
        for (r,k) in sorted(zip(list(map(str,list(self.keys()))),list(self.keys()))):
            s += "{0}: {1}, ".format(repr(k),self.get(k))
        return s[:len(s)-2] + "}"
