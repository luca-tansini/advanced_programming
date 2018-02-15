import sys

def decode(filename):
    f = open(filename)
    for i in range(0,4): next(f)
    i=0
    secret = ""
    char = 0
    for l in f:
        char ^= (int(l) & 1) << (i%7)
        i += 1
        if(i%7 == 0):
            secret += chr(char)
            if(char == 0): return secret
            char = 0

if __name__ == '__main__':
    print(decode(sys.argv[1]))
