dict =  {"A":10, "B":11, "C":12, "D":13, "E":14,
"F":15, "G":16, "H":17, "I":34, "J":18, "K":19,
"L":20, "M":21, "N":22, "O":35, "P":23, "Q":24,
"R":25, "S":26, "T":27, "U":28, "V":29, "W":32,
"X":30, "Y":31, "Z":33}

ID=input(str())
n1= dict[ID[0]]
sum= (n1%10)*9+n1//10

myID=ID[1:9]
add=0
t=1
for i in reversed(myID):
    if t<9:
        i=int(i)
        add=add+t*i
        t+=1

last=int(ID[9])
total= sum+ add+ last

if total%10==0:
    print ("real")
else:
    print ("fake")
    

    
        