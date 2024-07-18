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
def ryd(n):
    ss=0
    while n>0:
        if(n%10)%2==0:
            ss+=1
            if ss>1:
                return 0
        else:
            ss-=1
            if ss<0:
                ss=0
        n=n//10
    return 1

sum=0
for i in range(100000,1000000):
    ch=i
    num=0
    while ch>0:
        num+=ch%10
        ch=ch//10
    if primed(num) and ryd(i):
        sum+=1
print(sum)

