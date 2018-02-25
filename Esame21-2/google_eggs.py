def f(floorsleft,floorsdiff):
    if(floorsleft <= floorsdiff):
        print("throw#{1} at floor#{2}: {0} + {1}".format(floorsleft-1,1,floorsleft))
        return 2
    else:
        nthrows = f(floorsleft-floorsdiff,floorsdiff+1)
        print("throw#{1} at floor#{2}: {0} + {1}".format(floorsdiff-1,nthrows,floorsleft))
        return nthrows+1

def bestMaxThrows(floors):
    f(floors,1)
