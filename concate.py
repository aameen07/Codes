n=int(input())
m=int(input())
p = int(input())
e = int(input())
count=0
if (p==n)and (e==m):
    count+=1
else:
    for i in range(p,n):
        count+=1
    for j in range (e,m+1):
        count += 1
print(count)
