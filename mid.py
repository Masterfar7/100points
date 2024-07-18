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
def diff(n):
    ch=n
    a=[0]*10
    while ch>0:
        a[ch%10]+=1
        ch=ch//10
    for i in range(10):
        if a[i]>1:
            return 0
    return 1
sum=0
for i in range(100000,1000000):
    ch=i
    num=0
    while ch>0:
        num+=ch%10
        ch=ch//10
    if primed(num) and diff(i):
        sum+=1
print(sum)

