n = input()
a = int (n)
n = len (str(n))

x=0
for i in reversed(range(n)):

    x = int (a/10**i)
    print(x)
    x = a-x*10**i
    
    n+=1
    