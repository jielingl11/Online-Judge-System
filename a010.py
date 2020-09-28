while True:
    try:
        n= int(input())
    except:
        break
    
    display=""
    start=1
    i=2
    while i<=n:
        count=0
        

        while n%i==0:
            n=n/i
            count+=1
        
        if start==1:
            if count==1:
                display=str(i)
                start+=1
            
            elif count>=1:
                display=str(i)+"^"+str(count)
                start+=1
        
        else:
            if count==1:
                display=display+" * "+str(i)
            elif count>1:
                display=display+" * "+str(i)+"^"+str(count)
        i+=1
        
    print (display) 
            