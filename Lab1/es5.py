def cat(filenames):
    for file in filenames:
        try:
            fp = open(file)
            print("\nContent of file \"" + file + "\":\n");
            print(fp.read())
            fp.close()
        except Exception as e:
            print("\nFile \""+ file + "\" non esistente!\n")

# La parte su chmod non so come farla senza usare os.chmod...

def more(filename):
    try:
        fp = open(filename)
        print("\nContent of file \"" + filename + "\":\n");
        i=0;
        for line in fp:
            if(i%30==0 and i!=0):
                input()
                print("\x1B[1A",end='')
            print("{0:3d} ".format(i),end='')
            print(line, end='')
            i+=1

        fp.close()
    except Exception as e:
        print("\nFile \""+ file + "\" non esistente!\n")
