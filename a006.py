a,b,c= map(int, input().split())
D= b**2-4*a*c
if D>0:
    x1= int((-b+ D**0.5)/ (2*a))
    x2= int((-b- D**0.5)/ (2*a))
    print ("Two different roots x1=",x1," , x2=",x2, sep='')
elif D == 0:
    x1= int((-b+ D**0.5)/ (2*a))
    print ("Two same roots x=", x1, sep='')
else:
    print ("No real root")