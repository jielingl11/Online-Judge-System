t = int(input())

for i in range(1,t+1):
    a,b,c,d = map(int, input().split())

    if b/a == c/b:
        e= d*b/a
        print (a, b, c, d, int(e))
    else:
        e= d+b-a
        print (a, b, c, d, int(e))






