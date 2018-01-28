def trimTitles(file):
    out = []
    for l in open(file):
        l = l.replace('\n','')
        l = l.split(' ')
        l = [t for t in l if t not in ['','\t']]
        l = ' '.join(l)
        out += [l]
    return out

minor_words = ['the','and']

def makeAndFilterRotations(list):
    out = []
    for i in range(0,len(list)):
        l = list[i].split(' ')
        for n in range(0,len(l)):
            if(len(l[n]) > 2 and l[n].lower() not in minor_words):
                right = ' '.join(l[n:len(l)])
                left  = ' '.join(l[0:n])
                out += [(right,left,i)]
    return out

def sortRotations(rotations):
    return sorted(rotations,key = lambda r: r[0].lower())

class KWIC:
    def __init__(self,inputfile):
        titles = trimTitles(inputfile)
        self.kwic = sortRotations(makeAndFilterRotations(titles))

    def __repr__(self):
        out = ''
        for i in self.kwic:
            n = i[2]
            left = i[1][-33:]
            right = i[0][0:40]
            out += "{0:5d} {1:>33s} {2}\n".format(n,left,right)
        return out

if __name__ == '__main__':
    print("\n"+" "*32+"KWIC di titles.txt:\n\n")
    print(KWIC('titles.txt'))
