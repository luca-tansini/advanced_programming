len = int(input("inserisci lunghezza: "))
sum = 0
for i in range(0,len-1):
    sum += int(input())
x = ((len*(len+1))//2) - sum
print("manca: "+str(x))
