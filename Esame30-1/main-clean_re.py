from clean_re import *

if __name__ == '__main__':
    for l in open("clean_re.txt"):
        print(l)
        print(re_subject(l))
        print("*"*60)
