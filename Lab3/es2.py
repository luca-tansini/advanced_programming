class AlgebraicStructure:
    def buildcouples(self):
        a = []
        for e in self.set:
            a += [e]*len(self.set)
        b = self.set * len(self.set)**2
        return zip(a,b)

    def checkclosure(self):
        for (a,b) in self.buildcouples():
            if not (self.add(a,b) in self.set): return False,(a,b)
        return True

    def buildtriples(self):
        set = self.set
        l = len(set)
        a,b = [],[]
        for e in set:
            a += [e]*l**2
            b += [e]*l
        b = b*l
        c = set*(l**2)
        return zip(a,b,c)

    def checkassociativity(self):
        add = self.add
        for (a,b,c) in self.buildtriples():
            if(add(a,add(b,c)) != add(add(a,b),c)): return False,(a,b,c)
        return True

    def checkidentity(self):
        add = self.add
        for e in self.set:
            if(not( add(e,self.identity) == add(self.identity,e) == e)):return False,e
        return True

    def checkinvertibility(self):
        for a in self.set:
            if len([b for b in self.set if (self.add(a,b)==self.add(b,a)==self.identity)]) == 0 : return False,a
        return True

class Monoid(AlgebraicStructure):
    def __init__(self,set,add,identity):
        self.set = list(set)
        self.add = add
        self.identity = identity

    def checkmonoid(self):
        print("check closure..." + str(self.checkclosure()))
        print("check associativity..." + str(self.checkassociativity()))
        print("check identity..." + str(self.checkidentity()))

class Group(AlgebraicStructure):
    def __init__(self,set,add,identity):
        self.set = list(set)
        self.add = add
        self.identity = identity

    def checkgroup(self ):
        print("check closure..." + str(self.checkclosure()))
        print("check associativity..." + str(self.checkassociativity()))
        print("check identity..." + str(self.checkidentity()))
        print("check invertibility..." + str(self.checkinvertibility()))

class Ring:
    def __init__(self,set,add,addidentity,mul,mulidentity):
        self.set = set
        self.add = add
        self.addidentity = addidentity
        self.mul = mul
        self.mulidentity = mulidentity
        self.group = Group(set,add,addidentity)
        self.monoid = Monoid(set,mul,mulidentity)

    def checkdistributivity(self):
        for (a,b,c) in self.group.buildtriples():
            if not(self.mul(a,self.add(b,c)) == self.add(self.mul(a,b),self.mul(a,c))): return False,(a,b,c)
            if not(self.mul(self.add(a,b),c) == self.add(self.mul(a,c),self.mul(b,c))): return False,(a,b,c)
        return True

    def checkring(self):
        print("check additive group..." + str(self.group.checkgroup()))
        print("check multiplicative monoid..." + str(self.monoid.checkmonoid()))
        print("check distributivity..." + str(self.checkdistributivity()))

#Monoidi
boolean = Monoid({True,False}, lambda x,y: x or y, False)
boolean.checkmonoid()
Z6 = Monoid({0,1,2,3,4,5}, lambda x,y: (x+y)%6, 0)
Z6.checkmonoid()
#Gruppi
Z7 = Group({1,2,3,4,5,6}, lambda x,y: (x*y)%7, 1)
Z7.checkgroup()
#Anelli
Zero = Ring({0},lambda x,y:x+y,0,lambda x,y:x*y,0)
Zero.checkring()
Z10 = Ring({0,1,2,3,4,5,6,7,8,9},lambda x,y:(x+y)%10,0,lambda x,y: (x*y)%10,1)
Z10.checkring() 
