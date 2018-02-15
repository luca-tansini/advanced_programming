import sys

def diet(menu):
    if(menu == []): return 0,[]
    tota, dieta = recdiet(menu[1:],[menu[0]])
    totb, dietb = diet(menu[1:])
    if(tota > totb):
        return sum(dieta), dieta
    else:
        return sum(dietb), dietb

def recdiet(menu,diet):
    try:
        while(menu[0] > diet[-1]): del(menu[0])
    except Exception as e:
        return sum(diet),diet
    tota, dieta = recdiet(menu[1:],diet+[menu[0]])
    totb, dietb = recdiet(menu[1:],diet)
    if(tota > totb):
        return sum(dieta), dieta
    else:
        return sum(dietb), dietb

if __name__ == '__main__':
    f = open(sys.argv[1])
    next(f)
    menu = []
    for l in f:
        menu += [int(l)]
    diet = diet(menu)[1]
    print(len(diet),diet)
