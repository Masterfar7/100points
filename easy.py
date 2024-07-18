def primed(n):
    deli=0
    for i in range(2,n):
        if n%i==0:
            deli+=1
            break
    if deli==0:
        return 1
    else:
        return 0
sum=0
for i in range(100000,1000000):
    ch=i
    num=0
    while ch>0:
        num+=ch%10
        ch=ch//10
    if primed(num):
        sum+=1
print(sum)

