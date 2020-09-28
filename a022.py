n= str(input())
reverse=""

for i in reversed(n):
    reverse=reverse+i

if n==reverse:
    print("yes")
else:
    print("no")