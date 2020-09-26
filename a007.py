while True:
    try:
        n = int(input())
    except:
        break
    if n%6==0 or n%6==2 or n%6==3 or n%6==4:
        print ("非質數")

    if n%6==1 or n%6==5:
        k=int(n**0.5)
        for i in range (2,k):
            if n % i ==0:
                print ("非質數")
                break     
        else:
            print ("質數")       
