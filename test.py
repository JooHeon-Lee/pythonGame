cycle = 1
a = int(input())
ipVal = a

while True:
    if a == 0:
        print(cycle)
        break
    elif a == 1:
        print(60)
        break
    elif a < 10:
        a = "0" + str(a)
        
    a = int(a)
    c1 = int(a / 10) # 앞자리
    c2 = int(a % 10) # 뒷자리
    n = c1 + c2
    if n > 9:
        n = n % 10
    n2 = int(str(c2) + str(n))
    a = n2
    if a != ipVal:
        cycle +=1
    elif a == ipVal:
        print(cycle)
        break
        