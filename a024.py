a,b = map(int, input().split())

while a!=0 and b!=0:
    if a>b:
        a= a%b
    elif b>a:
        b= b%a
        
print (max(a,b))