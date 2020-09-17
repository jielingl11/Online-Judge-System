while True:
    try:
        Y= int(input())
    except:
        break
    if Y % 4 ==0 and Y % 100 !=0 or Y % 400 ==0 :
        print ("閏年")
    else:
        print ("平年")
    
