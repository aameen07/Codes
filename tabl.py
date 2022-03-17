c=[]
def table(k,a):
    for i in range(1,a*k):
        i=i*k
        c.append(i)
    return c    
def digits(k,a):
    for i in range(1,a**k):
        if i%10==k:
            c.append(i)
        else:
            i=i//10
            if i%10==k:
                c.append(i)
    return c
    
    
a=(int(input("a")))
k=(int(input("k")))
result1 = digits(k, a)
result=table(k,a)
print(result1)
print(result)
