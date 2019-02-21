#contando i piani da 1 (un palazzo di k piani arriva fino al k-esimo piano)
#l'idea sottostante è un ciclo che fa la somma dei primi n numeri finchè n < floors che viene poi sviluppato al contrario
def f(floorsleft,floorsdiff):
    if(floorsleft <= floorsdiff):
        print("throw#{1} at floor#{2}: ({0} throw(s) if it breaks) + ({1} throw(s) already done)".format(floorsleft-1,1,floorsleft))
        return 2
    else:
        nthrows = f(floorsleft-floorsdiff,floorsdiff+1)
        print("throw#{1} at floor#{2}: ({0} throw(s) if it breaks) + ({1} throw(s) already done)".format(floorsdiff-1,nthrows,floorsleft))
        return nthrows+1

def bestMaxThrows(floors):
    worst = f(floors,1)-1
    print("nel caso peggiore servono "+str(worst)+" lanci")
    return worst

#versione scema sottostante
def dumb(floors):
    i = 1
    t = 0
    while(t < floors):
        t += i
        i += 1
    return i-1
