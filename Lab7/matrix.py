import copy

class Matrix:
    def __init__(self,matrix):
        #la matrice si considera una lista di righe
        self.matrix = matrix

    def getdimensions(self):
        m = len(self.matrix)
        n = len(self.matrix[0])
        return (m,n)

    def equals(self,other):
        return self.matrix == other.matrix

    def copy(self):
        return copy.deepcopy(self)

    def __add__(self,other):
        if(self.getdimensions() != other.getdimensions()): raise ValueError("Matrices have incompatible dimensions!")
        r = copy.deepcopy(self)
        n,m = self.getdimensions()
        for i in range(0,n):
            for j in range(0,m):
                r.matrix[i][j] += other.matrix[i][j]
        return r

    def __mul__(self,other):
        if(self.getdimensions()[1] != other.getdimensions()[0]): raise ValueError("Matrices have incompatible dimensions!")
        out = []
        n,m = self.getdimensions()
        p = other.getdimensions()[1]
        for i in range(0,n):
            row = []
            for j in range(0,p):
                row += [sum([self.matrix[i][k]*other.matrix[k][j] for k in range(0,m)])]
            out += [row]
        return Matrix(out)

    def findbiggerint(self):
        bigger = 0
        for i in self.matrix:
            for j in i:
                if(len(str(j))>bigger): bigger = len(str(j))
        return bigger

    def __repr__(self):
        out = ''
        for i in self.matrix:
            out+="| "
            for j in i:
                out+=("{0:"+str(self.findbiggerint())+"d} ").format(j)
            out+="|\n"
        return out[:-1]
