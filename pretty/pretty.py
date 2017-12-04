def pretty(f,n):
    for i in range(2**n):
        args = list(("{:0"+str(n)+"b}").format(i))
        out = eval("f("+",".join(args)+")")
        print(str(args) + ": " + str(out))
