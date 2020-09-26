n = str(input())

discode="" # 建立一個控的字串

for i in n:
    a = ord(i)-7 
    discode=discode+chr(a)

print(discode)

