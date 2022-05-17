import math

a=int(input())
for i in range(a):
    b=list(map(int,input().strip().split()))

l=[]

for j in b:
    for i in range(1,j+1):
        if j%i == 0:
            l.append(i)
    middle=l[math.ceil(len(l)/2)]
    print(middle)