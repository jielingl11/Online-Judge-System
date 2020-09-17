a,b,c,d = map(int, input().split())
e=0
while e<105:
    if b/a == c/b:
        e= d*b/a
        print (int(e))
        break
    if b-a == c-b:
        e= d+b-a
        print (int(e))
        break

